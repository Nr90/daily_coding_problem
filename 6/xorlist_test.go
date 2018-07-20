/*
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
*/
package xorlist

import (
	"testing"
)

func TestUintXORPointer(t *testing.T) {
	p := &xorNode{}
	if uintXORPointer(p, p) != 0 {
		t.Error("uint XOR of same pointer should be 0")
	}
}

func TestXorListAdd(t *testing.T) {
	n := xorNode{}
	for i := 1; i < 9; i++ {
		n.add(&xorNode{value: i})
	}
}

func TestXorListGet(t *testing.T) {
	n := xorNode{}
	for i := 1; i < 9; i++ {
		n.add(&xorNode{value: i})
	}

	indices := [4]int{0, 1, 7, 9}
	for i := range indices {
		if r := n.get(i); r.value != i {
			t.Errorf("Expected %d got %d", i, n.value)
		}
	}
}
