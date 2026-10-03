"""
    Valid Sudoku

    You are given a 9x9 Sudoku board. Write a function to determine if the board is valid. Only the filled cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Return True if the board is valid, otherwise return False.

    A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be valid according to the Sudoku rules.

    Example 1:
    Input: board =
    [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
    Output: true

    Input: board =
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

    Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""


def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Determines if a given 9x9 Sudoku board is valid according to Sudoku rules.

    Args:
        board (list[list[str]]): A 9x9 list of lists representing the Sudoku board, where each cell contains a digit '1'-'9' or '.' for empty cells.

    Returns:
        bool: True if the board is valid, False otherwise.
        
    Intuition:
        Use sets to track the numbers seen in each row, column, and 3x3 box. If a number is repeated in any row, column, or box, the board is invalid.
        For the 3x3 boxes, we can identify which box a cell belongs to using integer division (row // 3, col // 3).
        e.g., the cell (4, 5) belongs to the box (1, 1) because 4 // 3 = 1 and 5 // 3 = 1.

    Time Complexity: O(1), since the board size is fixed at 9x9, making the number of operations constant regardless of input size.
    Space Complexity: O(1), since the maximum number of unique digits is limited to 9 for rows, columns, and boxes.

    Steps:
        1. Initialize three dictionaries with sets as values to keep track of unique seen numbers in rows, columns, and boxes.
        2. Iterate through each cell in the board:
            - If the cell is not empty (i.e., not '.'), check if the number has already been seen in the corresponding row, column, or box.
            - If it has been seen, return False (the board is invalid).
            - If it hasn't been seen, add the number to the corresponding row, column, and box sets.
        3. If no duplicates are found after checking all cells, return True (the board is valid).
    """
    rows = {}
    cols = {}
    boxes = {}

    for r in range(len(board)):
        for c in range(len(board)):
            value = board[r][c]
            # Skip empty cells
            if value == ".":
                continue

            box = (r // 3, c // 3)  # Identify which 3x3 box we are in
            # Initialize sets for the current row, column, and box if they don't exist
            rows.setdefault(r, set())
            cols.setdefault(c, set())
            boxes.setdefault(box, set())

            # Check if the value already exists in the current row, column, or box
            if (value in rows[r]) or (value in cols[c]) or (value in boxes[box]):
                return False

            # Add the value to the current row, column, and box sets
            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    return True

if __name__ == "__main__":
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(isValidSudoku(board1))  # Output: True

    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board2))  # Output: False
    
