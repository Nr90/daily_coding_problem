#=
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
=#
using Test
using Combinatorics

function largest_product_of_three(l::Array{Int,1})
    return maximum(map(prod, combinations(l, 3)))
end

l = [-10; -10; 5; 2;]
@test largest_product_of_three(l) == 500
