package com.nr90.dailycodingproblem;

import junit.framework.TestCase;

/**
 * This problem was asked by Facebook.
 * Given an array of integers, write a function to determine whether the array
 * could become non-decreasing by modifying at most 1 element.
 * 
 * For example, given the array [10, 5, 7], you should return true,
 * since we can modify the 10 into a 1 to make the array non-decreasing.
 * 
 * Given the array [10, 5, 1], you should return false,
 * since we can't modify any one element to get a non-decreasing array.
 */
public class SolutionTest extends TestCase {
    public void testGivenTrue() {
        int[] arr = new int[]{10, 5, 7};
        assertTrue(Solution.canBeMadeSortedByRemovingOneElement(arr));
    }

    public void testGivenFalse() {
        int[] arr = new int[]{10, 5, 1};
        assertFalse(Solution.canBeMadeSortedByRemovingOneElement(arr));
    }
}
