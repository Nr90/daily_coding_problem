#=
This problem was asked by Google.

Given the root of a binary tree, return a deepest node.
For example, in the following tree, return d
    a
   / \
  b   c
 /
d
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


function finddeepest(tree::BinaryTree)
    deepest = [tree.head]
    depth = [0]
    maxdepth = [0]
    finddeepest!(tree.head, depth, maxdepth, deepest)
    return deepest[1].value
end


function finddeepest!(treenode::Union{TreeNode,Nothing},
                     depth,
                     maxdepth,
                     deepest)
    if treenode === nothing
        return
    end
    if depth[1] > maxdepth[1]
        maxdepth[1] = depth[1]
        deepest[1] = treenode
    end
    depth[1] += 1
    finddeepest!(treenode.left, depth, maxdepth, deepest)
    finddeepest!(treenode.right, depth, maxdepth, deepest)
    depth[1] -= 1
end


function exampletest()
    example = BinaryTree(
        TreeNode(
            'a',
            TreeNode(
                'b',
                TreeNode('d', nothing, nothing),
                nothing
            ),
            TreeNode('c', nothing, nothing)
        )
    )
    @test example.head.value == 'a'
    @test example.head.left.value == 'b'
    @test example.head.left.left.value == 'd'
    @test example.head.right.value == 'c'
    @test finddeepest(example) == 'd'
end


exampletest()
