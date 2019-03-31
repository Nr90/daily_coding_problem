#=
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
=#
using Test


bif(x,y,b) = x * b + abs(b-1) * y


function tests()
    @test bif(Int32(3), Int32(4), Int32(0)) == 4
    @test bif(Int32(3), Int32(4), Int32(1)) == 3
end


tests()
