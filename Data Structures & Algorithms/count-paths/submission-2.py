class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        # numbers of paths starting at current position = 
        # number of paths at position below current position + number of paths at position to the right of the current position
        memo = {}
        def dps(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            # base cases
            ## start one above of endpoint
            if x == m-2 and y == n-1:
                memo[(x, y)] = 1 
                return memo[(x, y)]

            ## start one left of endpoint
            if x == m-1 and y == n-2:
                memo[(x, y)] = 1 
                return memo[(x, y)]

            # move one down + move one right 
            ## but only if possible
            s = 0
            if x < m - 1:
                s += dps(x+1, y)
            
            if y < n - 1:
                s += dps(x, y+1)

            memo[(x, y)] = s
            return memo[(x, y)]

        return dps(0, 0)
        