package com.nr90.dailycodingproblem;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import java.util.LinkedList;

/**
 * This problem was asked recently by Google.
 * Given k sorted singly linked lists,
 * write a function to merge all the lists into one sorted singly linked list.
 */
public class SolutionTest extends TestCase {
    public void testMerge() {
        LinkedList<Integer> listOne = new LinkedList<Integer>();
        listOne.add(1);
        listOne.add(3);
        listOne.add(5);
        LinkedList<Integer> listTwo = new LinkedList<Integer>();
        listTwo.add(2);
        listTwo.add(4);
        listTwo.add(6);
        LinkedList<Integer> merged = Solution.merge(listOne, listTwo);
        for (int i = 0; i < 6; i++) {
            assertEquals((int)merged.get(i), i+1);
        }
    }
}
