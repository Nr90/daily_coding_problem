#=
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
=#
using Test

struct LinkedListNode{T}
    value::T
    next::Union{LinkedListNode{T},Nothing}
end

function reverse!(head::LinkedListNode)
end

head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, nothing)))
reverse!(head)
@test head.value == 3
@test head.next.value == 2
@test head.next.next.value == 1
