#=
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf'].
=#
using Test


mapping = Dict{Char,Array{Char,1}}(
    '2' => ['a', 'b', 'c'],
    '3' => ['d', 'e', 'f'],
    '4' => ['g', 'h', 'i'],
    '5' => ['j', 'k', 'l'],
    '6' => ['m', 'n', 'o'],
    '7' => ['p', 'q', 'r', 's'],
    '8' => ['t', 'u', 'v'],
    '9' => ['w', 'x', 'y', 'z'],
)


function possibleletters(digits::String)
    return sort(vec([join(letters) for letters in Base.product([mapping[d] for d in digits]...)]))
end


function tests()
    @test possibleletters("2") == ["a", "b", "c"]
    @test possibleletters("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    @test possibleletters("27") == ["ap", "aq", "ar", "as", "bp", "bq", "br", "bs", "cp", "cq", "cr", "cs"]
end


tests()
