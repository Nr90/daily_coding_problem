#=
This problem was asked by Facebook.

There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of
starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
=#
using Test


function steps_to_bottom_right(m::Array{Int64, 2}, x=1, y=1)
    s = size(m)
    if s[1] == x || s[2] == y
        return 1
    end
    steps_to_bottom_right(m, x+1, y) +
    steps_to_bottom_right(m, x, y+1)
end

m = [0 0]
@test steps_to_bottom_right(m) == 1

m = [0 0; 0 0]
@test steps_to_bottom_right(m) == 2

m = [
    0 0 0 0 0;
    0 0 0 0 0;
    0 0 0 0 0;
    0 0 0 0 0;
    0 0 0 0 0
]
@test steps_to_bottom_right(m) == 70
