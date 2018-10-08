/*
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)],
you should return [(1, 3), (4, 10), (20, 25)].
*/
var assert = require('assert');

function mergeOverlapping(intervals) {
  var merged = [];
  var n = intervals.length;
  while (n > 0) {
    min_index = getLowestStartIntervalIndex(intervals);
    min_int = intervals.splice(min_index, 1)[0]
    if (merged.length == 0 || min_int[0] > merged[merged.length-1][1])
      merged.push(min_int);
    else if (min_int[1] > merged[merged.length-1][1])
      merged[merged.length-1][1] = min_int[1];
    n--;
  }
  return merged
}

function getLowestStartIntervalIndex(intervals) {
  var min_i = -1;
  var min_v = Number.MAX_VALUE;
  for (var i = 0; i < intervals.length; i++) {
    if (intervals[i][0] < min_v) {
      min_v = intervals[i][0];
      min_i = i;
    }
  }
  return min_i
}

describe('Problem 77', function() {
  describe('MergeOverlapping()', function() {
    it('Given example', function() {
      assert.deepEqual(
        mergeOverlapping([[1, 3], [5, 8], [4, 10], [20, 25]]),
        [[1, 3], [4, 10], [20, 25]]
      );
    });
  });
  describe('MergeOverlapping() 2', function() {
    it('Partial overlap example', function() {
      assert.deepEqual(
        mergeOverlapping([[1, 3], [3, 6], [4, 10], [20, 25]]),
        [[1, 10], [20, 25]]
      );
    });
  });
});