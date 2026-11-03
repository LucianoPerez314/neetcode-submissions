from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        explored = {}
        # Step 1: Add all rotten fruit to the queue initially
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        # Step 2: Multi-source BFS
        while queue:
            r, c, minute = queue.popleft()
            # print(queue, r, c, minute)
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # If the neighbor is within bounds and is a fresh fruit.
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    # If not in explored append it to the queue with the minute it has rotted.
                    if (nr, nc) not in explored:
                        queue.append((nr, nc, minute+1))
                        explored[(nr, nc)] = minute+1
                    else: # If in explored update the minimum minute it would've taken to rot it.
                        explored[(nr, nc)] = min(minute+1, explored[(nr, nc)])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in explored:
                    return -1
        
        if not explored:
            return 0

        return max(explored.values())