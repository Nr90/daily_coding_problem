"""
This problem was asked by Google.

Implement a file syncing algorithm for two computers
over a low-bandwidth network.
What if we know the files in the two computers are mostly the same?
"""
import unittest
import collections
import hashlib
import zlib

# solution from:
# https://tylercipriani.com/blog/2017/07/09/the-rsync-algorithm-in-python/

BLOCK_SIZE = 4096

Signature = collections.namedtuple('Signature', 'md5 adler32')


class Chunks(object):
    """
    Data stucture that holds rolling checksums for file B
    """
    def __init__(self):
        self.chunks = []
        self.chunk_sigs = {}

    def append(self, sig):
        self.chunks.append(sig)
        self.chunk_sigs.setdefault(sig.adler32, {})
        self.chunk_sigs[sig.adler32][sig.md5] = len(self.chunks) - 1

    def get_chunk(self, chunk):
        adler32 = self.chunk_sigs.get(adler32_chunk(chunk))

        if adler32:
            return adler32.get(md5_chunk(chunk))

        return None

    def __getitem__(self, idx):
        return self.chunks[idx]

    def __len__(self):
        return len(self.chunks)


def checksums_file(fn):
    """
    Returns object with checksums of file
    """
    chunks = Chunks()
    with open(fn) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            chunks.append(
                Signature(
                    adler32=adler32_chunk(chunk),
                    md5=md5_chunk(chunk)
                )
            )

        return chunks


def md5_chunk(chunk):
    m = hashlib.md5()
    m.update(str.encode(chunk))
    return m.hexdigest()


def adler32_chunk(chunk):
    return zlib.adler32(str.encode(chunk))


def _get_block_list(file_one, file_two):
    """
    The good stuff.

    1. create rolling checksums file_two
    2. for each chunk in file one, determine if chunk is already in file_two
        a. If so:
            i. return the index of that chunk
            ii. move the read head by the size of a chunk
        b. If not:
            i. return the next byte
            ii. move the read head by 1 byte
    3. start over at 2 until you're out of file to read
    """
    checksums = checksums_file(file_two)
    blocks = []
    offset = 0
    with open(file_one) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            chunk_number = checksums.get_chunk(chunk)

            if chunk_number is not None:
                offset += BLOCK_SIZE
                blocks.append(chunk_number)
                continue
            else:
                offset += 1
                blocks.append(chunk[0])
                f.seek(offset)
                continue

    return blocks


def sync(file_one, file_two):
    """
    Essentially this returns file one, but in a fancy way :)

    The output from get_block_list is a list of either chunk indexes or data as
    strings.

    If it's a chunk index, then read that chunk from the file and append it to
    output. If it's not a chunk index, then it's actual data and should just be
    appended to output directly.
    """
    output = ''
    with open(file_two) as ft:
        for block in _get_block_list(file_one, file_two):
            if isinstance(block, int):
                ft.seek(block * BLOCK_SIZE)
                output += ft.read(BLOCK_SIZE)
            else:
                output += block

    return output


class TestSolution(unittest.TestCase):
    def test_given(self) -> None:
        self.assertEqual(sync('foo.txt', 'bar.txt'), 'foo')


if __name__ == '__main__':
    unittest.main()
