#=
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
=#
using Test
using Combinatorics


function find_nth_perfect_number(n::Int)
    perfect = 1
    i = 19
    while perfect != n
        i += 9
        if sum(digits(i)) == 10
            perfect += 1
        end
    end
    i
end


perfect = 0
for i in 1:100000
    if sum(digits(i)) == 10
        global perfect
        perfect += 1
        @test find_nth_perfect_number(perfect) == i
    end
end
