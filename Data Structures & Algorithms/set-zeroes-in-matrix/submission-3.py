class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        first_row, first_col = False, False
        # First pass: Mark first entry in current row and col as 0 indicating these need to be zeroed.
        for x in range(ROWS):
            for y in range(COLS):
                if matrix[x][y] == 0:
                    if x == 0:
                        first_row = True
                    if y == 0:
                        first_col = True
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        # Second pass: Iterate through inner matrix (not including first row and column and check if its marked for zeroing.)
        for x in range(1, ROWS):
            for y in range(1, COLS):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        # edge case
        if first_row:
            for y in range(COLS):
                matrix[0][y] = 0

        if first_col: 
            for x in range(ROWS):
                matrix[x][0] = 0
        return
        