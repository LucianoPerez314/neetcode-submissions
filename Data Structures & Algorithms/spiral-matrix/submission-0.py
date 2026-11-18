class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Recursive substructure
        # Matrix spiral = traversing edge of matrix + spiral of inner matrix.
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        def recurse(start_x, start_y):
            if len(res) >= ROWS * COLS:
                return 
            # Step 1: Walk through outer edge of matrix. 
            # 1.1 First row (left to right)
            for y in range(start_y, COLS-start_y):
                res.append(matrix[start_x][y])
            # 1.2 Last column (up to down) (excluding first row)
            for x in range(start_x+1, ROWS-start_x):
                res.append(matrix[x][COLS-1-start_y])
            # 1.3 Last row (right to left) (excluding last column and first row)
            if ROWS - 1 - start_x != start_x:
                for y in range(COLS - 2 - start_y, start_y - 1, -1):
                    res.append(matrix[ROWS - 1 - start_x][y])
            # 1.4 First column (down to up) (excluding last row and last column and first row)
            if COLS - 1 - start_y != start_y:
                for x in range(ROWS - 2 - start_x, start_x, -1):
                    res.append(matrix[x][start_y])

            recurse(start_x+1, start_y+1)
        # Recurse.
        recurse(0, 0)
        return res