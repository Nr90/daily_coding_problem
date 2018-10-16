package com.nr90.dailycodingproblem;
import java.util.LinkedList;

/**
 * This problem was asked recently by Google.
 * Given k sorted singly linked lists,
 * write a function to merge all the lists into one sorted singly linked list.
 */
public class Solution {
    public static LinkedList<Integer> merge(LinkedList<Integer> listOne, LinkedList<Integer> listTwo ) {
        LinkedList<Integer> merged = new LinkedList<Integer>();
        int i = 0;
        int j = 0;
        while (i < listOne.size() && j < listTwo.size()) {
            if (listOne.get(i) < listTwo.get(j)) {
                merged.add(listOne.get(i));
                i++;
            } else {
                merged.add(listTwo.get(j));
                j++;
            }
        }
        while (i < listOne.size()) {
            merged.add(listOne.get(i));
            i++;
        }
        while (j < listTwo.size()) {
            merged.add(listTwo.get(j));
            j++;
        }
        return merged;
    }
}
