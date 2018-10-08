/*
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed
to ensure that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center.
We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
*/
var assert = require('assert');

function minColumnsRemoved(m) {
  if (m.length == 1)
    return 0;
  var cols = 0;
  for (var i = 0; i < m[0].length; i++) {
    var previous = m[0][i];
    for (var j = 1; j < m.length; j++) {
      if (previous > m[j][i]) {
        cols++;
        break;
      }
      previous = m[j][i];
    }
  }
  return cols;
};

describe('Problem 76', function() {
  describe('minColumnsRemoved() 1', function() {
    it('Should return 1', function() {
      m = [
        ['c', 'b', 'a'],
        ['d', 'a', 'f'],
        ['g', 'h', 'i']
      ];
      assert.equal(minColumnsRemoved(m), 1);
    });
  });

  describe('minColumnsRemoved() 2', function() {
    it('Should return 0', function() {
      m = [
        ['a', 'b', 'c', 'd', 'e', 'f']
      ];
      assert.equal(minColumnsRemoved(m), 0);
    });
  });

  describe('minColumnsRemoved() 3', function() {
    it('Should return 1', function() {
      m = [
        ['z', 'y', 'x'],
        ['w', 'v', 'u'],
        ['t', 's', 'r']
      ];
      assert.equal(minColumnsRemoved(m), 3);
    });
  });
});