#=
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
=#
using Test


mutable struct TreeNode{T}
    value::T
    left::Union{TreeNode{T},Nothing}
    right::Union{TreeNode{T},Nothing}
end


mutable struct BinaryTree
    head::TreeNode
end


function invert!(tree::BinaryTree)
    flip!(tree.head)
end


function flip!(node::Union{TreeNode,Nothing})
    node.left, node.right = node.right, node.left
    if node.left !== nothing
        flip!(node.left)
    end
    if node.right !== nothing
        flip!(node.right)
    end
end


function exampletest()
    example = BinaryTree(
        TreeNode(
            'a',
            TreeNode(
                'b',
                TreeNode('d', nothing, nothing),
                TreeNode('e', nothing, nothing)
            ),
            TreeNode(
                'c',
                TreeNode('f', nothing, nothing),
                nothing)
        )
    )
    @test example.head.value == 'a'
    @test example.head.left.value == 'b'
    @test example.head.left.left.value == 'd'
    @test example.head.left.right.value == 'e'
    @test example.head.right.value == 'c'
    @test example.head.right.left.value == 'f'
    invert!(example)
    @test example.head.value == 'a'
    @test example.head.right.value == 'b'
    @test example.head.right.right.value == 'd'
    @test example.head.right.left.value == 'e'
    @test example.head.left.value == 'c'
    @test example.head.left.right.value == 'f'
end


exampletest()
