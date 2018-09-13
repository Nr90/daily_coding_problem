#=
This problem was asked by Google.

Implement integer exponentiation.
That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
=#

module Pow
export pow

function pow(x, y)
    exponentiation_by_squaring(1, x, y)
end

function exponentiation_by_squaring(y, x, n::Int)
    if n < 0
        return exponentiation_by_squaring(y, 1/x, -n)
    end
    if n == 0
        return y
    end
    if n == 1
        return x * y
    end
    if iseven(n)
        return exponentiation_by_squaring(y, x*x, div(n,2))
    end
    exponentiation_by_squaring(x*y, x*x, div(n-1,2))
end

end