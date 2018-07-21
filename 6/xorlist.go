package xorlist

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

import (
	"unsafe"
)

type xorNode struct {
	both  *xorNode
	value int
}

func uintXORPointer(p1, p2 *xorNode) uintptr {
	return uintptr(unsafe.Pointer(p1)) ^ uintptr(unsafe.Pointer(p2))
}

func uintToXORNode(p uintptr) *xorNode {
	return (*xorNode)(unsafe.Pointer(p))
}

func xorPointer(p1, p2 *xorNode) *xorNode {
	return uintToXORNode(uintXORPointer(p1, p2))
}

func (n *xorNode) add(e *xorNode) {
	if n.both == nil {
		n.both = e
		e.both = n
		return
	}
	last := n.findLast()
	last.both = xorPointer(last.both, e)
	e.both = last
}

func (n *xorNode) findLast() *xorNode {
	previous := n
	current := previous.both
	for {
		if current.both == previous {
			return current
		}
		next := xorPointer(current.both, previous)
		previous = current
		current = next
	}
}

func (n *xorNode) get(index int) *xorNode {
	if index == 0 {
		return n
	}
	if index == 1 {
		return n.both
	}
	previous := n
	current := previous.both
	for i := 0; i < index; i++ {
		next := xorPointer(current.both, previous)
		previous = current
		current = next
	}
	return previous
}
