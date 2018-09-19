"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1
and a sub-directory subdir2 containing a file file.ext.

The string:
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext
and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2,
 containing a file file2.ext.

We are interested in finding the longest (number of characters)
absolute path to a file within our file system.
For example, in the second example above,
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to a
file in the abstracted file system.
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""
import unittest
from typing import List


def get_path_len(fs_lines: List[str], l_idx: int) -> int:
    depth = fs_lines[l_idx].count('\t')
    path_len = len(fs_lines[l_idx][depth:]) + len(fs_lines[0]) + 1
    while depth > 1:
        l_idx -= 1
        assert l_idx > 0
        if fs_lines[l_idx].count('\t') == depth - 1:
            depth -= 1
            path_len += len(fs_lines[l_idx][depth:]) + 1
    return path_len


def longest_path(fs_str: str) -> int:
    lines = fs_str.split('\n')
    longest = 0
    for i, l in enumerate(lines):
        if '.' in l:
            longest = max(longest, get_path_len(lines, i))
    return longest


class TestSolution(unittest.TestCase):
    def test_given_large(self) -> None:
        fs_str = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'  # NOQA
        longest = len('dir/subdir2/subsubdir2/file2.ext')
        self.assertEqual(longest_path(fs_str), longest)

    def test_no_files(self) -> None:
        fs_str = 'dir\n\tsubdir1\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2'
        longest = 0
        self.assertEqual(longest_path(fs_str), longest)


if __name__ == '__main__':
    unittest.main()
