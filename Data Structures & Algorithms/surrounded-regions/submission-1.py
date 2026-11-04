from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        explored = set()

        def onEdge(row, col):
            return row == 0 or row == ROWS-1 or col == 0 or col == COLS-1

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in explored and onEdge(r, c):
                    queue.append((r, c))
        

        while queue:
            r, c = queue.popleft()
            board[r][c] = "S"
            explored.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O" and (nr, nc) not in explored:
                    queue.append((nr, nc))
        
        # print(board)
        for r in range(ROWS):
            for c in range(COLS):
                # print(board[r][c], board[r][c] == "O", board[r][c] == "S")
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

        return 
        