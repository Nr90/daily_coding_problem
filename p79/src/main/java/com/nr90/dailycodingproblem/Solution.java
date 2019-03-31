package com.nr90.dailycodingproblem;

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
public class Solution {
    public static boolean canBeMadeSortedByRemovingOneElement(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (isSortedWithoutOne(arr, i)) {
                return true;
            }
        }
        return false;
    }

    public static boolean isSortedWithoutOne(int[] a, int except) {
        for (int i = 0; i < a.length - 1; i++) {
            if (i == except) {
                continue;
            }
            if (a[i] > a[i + 1]) {
                return false;
            }
        }
        return true;
    }
}
