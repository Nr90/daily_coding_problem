#=
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
=#
using Test

function knights_tour(N)
    moves = 0
    for i in 1:N
        for j in 1:N
            board = zeros(Int, N, N)
            board[i, j] = 1
            moves += number_of_moves(board, i, j)
        end
    end
    moves
end

function number_of_moves(board::Array{Int, 2}, x, y)
    if length(board) == sum(board)
        return 1
    end
    pos_moves = find_possible_moves(board, x, y)
    solutions = 0
    for m in pos_moves
        board[m[1], m[2]] = 1
        solutions += number_of_moves(board, m[1], m[2])
        board[m[1], m[2]] = 0
    end
    solutions
end

function find_possible_moves(board::Array{Int, 2}, x, y)
    n, n = size(board)
    moves = Tuple{Int, Int}[]
    if x + 2 <= n && y + 1 <= n && board[x+2, y+1] == 0
        push!(moves, (x+2, y+1))
    end
    if x - 2 > 0 && y + 1 <= n && board[x-2, y+1] == 0
        push!(moves, (x-2, y+1))
    end
    if x + 2 <= n && y - 1 > 0 && board[x+2, y-1] == 0
        push!(moves, (x+2, y-1))
    end
    if x - 2 > 0 && y - 1 > 0 && board[x-2, y-1] == 0
        push!(moves, (x-2, y-1))
    end
    if x + 1 <= n && y + 2 <= n && board[x+1, y+2] == 0
        push!(moves, (x+1, y+2))
    end
    if x - 1 > 0 && y + 2 <= n && board[x-1, y+2] == 0
        push!(moves, (x-1, y+2))
    end
    if x + 1 <= n && y - 2 > 0 && board[x+1, y-2] == 0
        push!(moves, (x+1, y-2))
    end
    if x - 1 > 0 && y - 2 > 0 && board[x-1, y-2] == 0
        push!(moves, (x-1, y-2))
    end
    moves
end

solutions = [1 0 0 0 1728 6637920 165575218320 19591828170979904]
for i in 1:5
    @test knights_tour(i) == solutions[i]
end
