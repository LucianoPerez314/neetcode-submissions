from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_queue, p_explored = deque(), set()
        atlantic_queue, a_explored = deque(), set()
        for r in range(ROWS):
            for c in range(COLS):
                pacific, atlantic = (r == 0 or c == 0), (r == ROWS - 1 or c == COLS - 1)
                if pacific: 
                    pacific_queue.append((r, c))
                if atlantic: 
                    atlantic_queue.append((r, c))

        while pacific_queue:
            r, c = pacific_queue.popleft()
            p_explored.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] \
                 and (nr, nc) not in p_explored:
                    pacific_queue.append((nr, nc))
        
        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            a_explored.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] \
                 and (nr, nc) not in a_explored:
                    atlantic_queue.append((nr, nc))
        
        res = []
        for r, c in p_explored:
            if (r, c) in a_explored:
                res.append([r, c])
        return res