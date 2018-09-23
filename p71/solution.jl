#=
This problem was asked by Two Sigma.

Using a function rand7()
    that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5()
    that returns an integer from 1 to 5 (inclusive).
=#
using Test

function rand7()
    rand(1:7)
end

function rand5()
   result = rand7()
    while result > 5
        result = rand7()
    end
    result
end

function test_rand5_dist()
    dist = zeros(Int, 5)
    runs = 500000
    for _ in 1:runs
        n = rand5()
        dist[n] += 1
        @test n >= 1 && n <= 7
    end
    mean = runs / 5
    for n in dist
        @test abs(n - mean) < runs / 100
    end
end

test_rand5_dist()
