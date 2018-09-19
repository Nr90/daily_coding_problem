#=
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9
grid with digits.
The objective is to fill the grid with the constraint that
every row, column, and box (3 by 3 subgrid) must contain
all of the digits from 1 to 9.

Implement an efficient sudoku solver.
=#

module Sudoku
export solve

# Check if the number is already used in the given row
function valid_in_row(sudoku, number, row)
    for i in 1:9
        if sudoku[row, i] == number
            return false
        end
    end
    return true
end

# Check if the number is already used in the given column
function valid_in_col(sudoku, number, col)
    for i in 1:9
        if sudoku[i, col] == number
            return false
        end
    end
    return true
end

# Check if the number is already used in the given 3x3 box
function valid_in_box(sudoku, number, row, col)
    # Find where 3x3 row and col starts
    col_start = col - (col-1) % 3
    row_start = row - (row-1) % 3
    # Loop through the 3 columns and 3 rows
    for i in 0:2
        for z in 0:2
            if sudoku[i+row_start, z+col_start] == number
                return false
            end
        end
    end
    return true
end

function position_valid(sudoku, number, row, col)
    return valid_in_row(sudoku, number, row) &&
           valid_in_col(sudoku, number, col) &&
           valid_in_box(sudoku, number, row, col)
end

# Find if there are any empty cells left
function check_complete(sudoku)
    for row in 1:9
        for col in 1:9
            if sudoku[row, col] == 0
                return false, row, col
            end
        end
    end
    return true, 0, 0
end

function solve(sudoku)
    complete, row, col = check_complete(sudoku)
    if complete
        return true
    end

    # Try numbers from 1
    for posssible_number in 1:9
        if position_valid(sudoku, posssible_number, row, col)
            sudoku[row, col] = posssible_number

            # If solved, propegate up the callstack
            if solve(sudoku)
                return true
            end

            # backtrack
            sudoku[row, col] = 0
        end
    end
    return false
end

end