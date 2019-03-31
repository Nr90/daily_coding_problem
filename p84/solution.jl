#=
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water,
so an island is a group of 1s that are neighboring and their perimiter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
=#
using Test


function islands(m::Array{Int, 2})
    islands = 0
    seen = zeros(Bool, size(m))
    for j = 1:size(m,2)
        for i = 1:size(m,1)
            m[i,j] == 1 || continue

            # right of found land
            if j < size(m,2) && m[i,j+1] == 1
                seen[i,j+1] = true
            end

            # top right of found land
            if j < size(m,2) && i > 1 && m[i-1,j+1] == 1
                seen[i-1,j+1] = true
            end

            # bottom right of found land
            if j < size(m,2) && i < size(m,1) && m[i+1,j+1] == 1
                seen[i+1,j+1] = true
            end

            # below found land
            if i < size(m,1) && m[i+1,j] == 1
                seen[i+1,j] = true
            end

            # bottom left of found land
            if j < size(m,2) && i < size(m,1) && j > 1 && m[i+1,j-1] == 1
                seen[i+1,j-1] = true
            end

            seen[i,j] == false || continue
            islands += 1
        end
    end
    return islands
end


function tests()
    m = [
        1 0 0 0 0;
        0 0 1 1 0;
        0 1 1 0 0;
        0 0 0 0 0;
        1 1 0 0 1;
        1 1 0 0 1
    ]
    @test islands(m) == 4
end


tests()
