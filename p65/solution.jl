#=
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
=#

function print_clockwise(m::Array{Int, 1})
    for e in m
        println(e)
    end
end

function print_clockwise(m::Array{Int, 2})
    rows, cols = size(m)
    print_top_row(m)
    if cols > 1
        print_right_col(m)
    end
    if rows > 1
        print_bottom_row(m)
    end
    if cols > 1
        print_left_col(m)
    end
    if rows > 2
        print_clockwise(m[2:rows-1, 2:cols-1])
    end
end

function print_top_row(m::Array{Int, 2})
    for nr in m[1, :]
        println(nr)
    end
end

function print_right_col(m::Array{Int, 2})
    for nr in m[2:end, end]
        println(nr)
    end
end

function print_bottom_row(m::Array{Int, 2})
    for nr in m[end, end-1:-1:1]
        println(nr)
    end
end

function print_left_col(m::Array{Int, 2})
    for nr in m[end-1:-1:2, 1]
        println(nr)
    end
end

m = [
    1  2  3  4  5;
    6  7  8  9  10;
    11 12 13 14 15;
    16 17 18 19 20
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()

m = [
    1  2  3  4  5;
    6  7  8  9  10;
    11 12 13 14 15
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()

m = [
    1 2 3 4 5
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()

m = [
    1; 2; 3; 4; 5
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()

m = [
    1  2;
    3  4
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()

m = [
    1  2;
    3  4;
    5  6
]
display(m)
println("\nClockwise:")
print_clockwise(m)
println()
