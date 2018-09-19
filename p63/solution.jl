#=
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word,
write a function that returns whether the word can be
found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last row.
=#
using Test

function can_be_found(m::Array{Char, 2}, target) Bool
    left_to_right(m, target) || up_to_down(m, target)
end

function left_to_right(m::Array{Char, 2}, target) Bool
    s = size(m)
    if length(target) > s[2]
        return false
    end
    for i in 1:s[1]
        if occursin(target, join(m[i, :]))
            return true
        end
    end
    return false
end

function up_to_down(m::Array{Char, 2}, target) Bool
    s = size(m)
    if length(target) > s[1]
        return false
    end
    for i in 1:s[2]
        if occursin(join(m[:, i]), target)
            return true
        end
    end
    return false
end

given = [
    'F' 'A' 'C' 'I';
    'O' 'B' 'Q' 'P';
    'A' 'N' 'O' 'B';
    'M' 'A' 'S' 'S'
]
@test can_be_found(given, "MASS") == true
@test can_be_found(given, "FOAM") == true
@test can_be_found(given, "NOB") == true
@test can_be_found(given, "elbert") == false
@test can_be_found(given, "faci") == false
