#=
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
=#
using Test


mutable struct LinkedListNode{T}
    value::T
    next::Union{LinkedListNode{T},Nothing}
end


mutable struct LinkedList
    head::LinkedListNode
end


function reverse!(list::LinkedList)
    prev = nothing
    current = list.head
    next = current.next

    while current != nothing
        current.next = prev
        prev = current
        current = next
        if next != nothing
            next = next.next
        end
    end
    list.head = prev
end

list = LinkedList(LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, nothing))))
reverse!(list)
@test list.head.value == 3
@test list.head.next.value == 2
@test list.head.next.next.value == 1
