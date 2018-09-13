#=
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
=#
push!(LOAD_PATH, ".")
using Pow
using Test

for x in -10:10
    for y in 0:10
        @test pow(x, y) == x^y
    end
end