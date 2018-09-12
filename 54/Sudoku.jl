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

# Check if the position is valid for the given number by checking all three conditions above
function position_valid(sudoku, number, row, col)
    return valid_in_row(sudoku, number, row) &&
           valid_in_col(sudoku, number, col) &&
           valid_in_box(sudoku, number, row, col)
end

next_empty_pos = [1 1]
# Find if there are any empty cells left and assign the next empty cell
function empty_position_exists(sudoku)
    for row in 1:9
        for col in 1:9
            if sudoku[row, col] == 0
                global next_empty_pos
                next_empty_pos = [row col]
                return true
            end
        end
    end
    return false
end

function solve(sudoku)
    # If there are no more empty cells, we are finished
    if !empty_position_exists(sudoku)
        return true
    end
    row = next_empty_pos[1]
    col = next_empty_pos[2]

    # Try numbers from 1
    for posssible_number in 1:9
        if position_valid(sudoku, posssible_number, row, col)
            sudoku[row, col] = posssible_number

            # If the next function call evalutes to true, then this should be true as well
            if solve(sudoku)
                return true
            end

            # If the above did not work then, set the number back to 0 (unassgined)
            sudoku[row, col] = 0
        end
    end
    return false
end

end