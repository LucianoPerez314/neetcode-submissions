class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ones.add((row, col))
        
        islands = 0
        while len(ones) > 0:
            start = ones.pop()
            islands += 1
            bfs(start, grid, ones)
        return islands


def bfs(start, grid, ones):
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    frontier, explored = [start], set()
    while len(frontier) > 0:
        curr_r, curr_c = frontier.pop()
        explored.add((curr_r, curr_c))
        if (curr_r, curr_c) in ones:
            ones.remove((curr_r, curr_c))
        grid[curr_r][curr_c] = "0"

        for dr, dc in neighbors:
            if (0 <= curr_r + dr and curr_r + dr < len(grid)) and \
            (0 <= curr_c + dc and curr_c + dc < len(grid[0])) and \
            grid[curr_r+dr][curr_c+dc] == "1" and \
            (curr_r + dr, curr_c + dc) not in explored:
                frontier.append((curr_r + dr, curr_c + dc))