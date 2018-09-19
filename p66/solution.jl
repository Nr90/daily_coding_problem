#=
This problem was asked by Square.

Assume you have access to a function toss_biased()
    which returns 0 or 1 with a probability that's not 50-50
    (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
=#
using Test

function  toss_biased()
    rand() + 0.2 > 0.5 ? 1 : 0
end

function toss_unbiased()
    flip1 = toss_biased()
    flip2 = toss_biased()
    if flip1 == 0 && flip2 == 1
        return 0
    end
    if flip1 == 1 && flip2 == 0
        return 1
    end
    toss_unbiased()
end

function do_n_tosses(toss_func, n)
    zero_tosses, one_tosses = 0, 0
    for _ in 1:n
        if toss_func() == 1
            one_tosses += 1
        else
            zero_tosses += 1
        end
    end
    zero_tosses, one_tosses
end

n = 10000000
results = do_n_tosses(toss_unbiased, n)
@test isapprox(results[1]/n, results[2]/n, rtol=0.001)
