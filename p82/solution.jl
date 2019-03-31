#=
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
=#
using Test


function reader(content::String)
    first = 1
    function read7()
        last = first + 6 < length(content) ? first + 6 : length(content)
        next = content[first:last]
        first += 7
        return next
    end
    return read7
end


function readN(n)
    result = join([read7() for _ in 1:ceil(n/7)])
    return result[1:minimum([n, length(result)])]
end


function tests()
    global read7
    read7 = reader("Hello world")
    @test read7() == "Hello w"
    @test read7() == "orld"
    @test read7() == ""
    read7 = reader("Hello world")
    @test readN(5) == "Hello"
    read7 = reader("Hello world")
    @test readN(11) == "Hello world"
    read7 = reader("Hello world")
    @test readN(13) == "Hello world"
end


tests()
