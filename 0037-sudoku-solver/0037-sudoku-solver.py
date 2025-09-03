class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # n = size of each small box (3x3), N = total size of board (9x9)
        n, N = 3, 9

        # Track usage of numbers in rows, columns, and 3x3 boxes
        # rows[i][d] = how many times digit d has been placed in row i
        rows = [[0] * (N + 1) for _ in range(N)]
        cols = [[0] * (N + 1) for _ in range(N)]
        boxes = [[0] * (N + 1) for _ in range(N)]

        # Flag to mark when the sudoku has been solved
        sudokuSolved = False

        # Helper: check if we can place digit d at position (row, col)
        def couldPlace(d, row, col):
            # Find which box (0–8) the cell belongs to
            idx = (row // n) * n + col // n
            # If digit d is not already used in this row, col, and box
            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0

        # Helper: place digit d at (row, col) and update constraints
        def placeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[idx][d] += 1
            board[row][col] = str(d)

        # Helper: remove digit d from (row, col) → backtracking undo
        def removeNumber(d, row, col):
            idx = (row // n) * n + col // n
            rows[row][d] -= 1
            cols[col][d] -= 1
            boxes[idx][d] -= 1
            board[row][col] = '.'

        # Helper: move to the next cell
        def placeNextNumbers(row, col):
            nonlocal sudokuSolved
            # If we are at the last cell and filled it successfully
            if row == N - 1 and col == N - 1:
                sudokuSolved = True
            # If at end of row → go to next row
            elif col == N - 1:
                backtrack(row + 1, 0)
            # Otherwise, just move right to next column
            else:
                backtrack(row, col + 1)

        # Main backtracking function
        def backtrack(row, col):
            nonlocal sudokuSolved
            # If the current cell is empty
            if board[row][col] == '.':
                # Try digits 1–9
                for d in range(1, 10):
                    if couldPlace(d, row, col):
                        # Place digit
                        placeNumber(d, row, col)
                        # Move to next cell
                        placeNextNumbers(row, col)
                        # If not solved yet, undo and try next digit
                        if not sudokuSolved:
                            removeNumber(d, row, col)
            else:
                # If already filled, just go to next cell
                placeNextNumbers(row, col)

        # Initialize the constraints with the given board
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)

        # Start solving from the top-left cell
        backtrack(0, 0)
