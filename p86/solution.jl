#=
This problem was asked by Google.

Given a string of parentheses,
write a function to compute the minimum number of parentheses to be removed
to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
=#
using Test


function validate(s)
    close_without_open = 0
    opens = 0
    for c in s
        if c == '('
            opens += 1
            continue
        end
        # c == ')'
        if opens < 1
            close_without_open += 1
            continue
        end
        opens -= 1
    end
    return opens + close_without_open
end


function tests()
    @test validate("()()()") == 0
    @test validate("()())()") == 1
    @test validate(")(") == 2
end


tests()
