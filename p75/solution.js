/*
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
*/
var assert = require('assert');

Array.prototype.longestIncreasingSubsequence = function() {
  n = this.length;
  lis = Array(n).fill(1)
  for (var i = 1; i < n; i++) {
    for (var j = 0; j < i; j++) {
      if (this[i] > this[j] && lis[i] < lis[j] + 1) {
        lis[i] = lis[j] + 1;
      }
    }
  }
  maximum = 0
  for (var i = 0; i < n; i++) {
    maximum = maximum > lis[i] ? maximum : lis[i]
  }
  return maximum
};


describe('Array', function() {
  describe('#longestIncreasingSubsequence()', function() {
    it('should return 6: 0, 2, 6, 9, 11, 15', function() {
      assert.equal([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15].longestIncreasingSubsequence(), 6);
    });
  });
});