# Sudoku Solver using Backtracking

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Empty cell
                return (i, j)
    return None

def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # No empty cells means puzzle is solved
    
    row, col = empty_location

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack if solution not found

    return False

# Test the solver with an example Sudoku puzzle
if __name__ == "__main__":
    # 0 represents empty cells
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("Solved Sudoku Puzzle:")
        print_board(sudoku_board)
    else:
        print("No solution exists for the given puzzle.")
