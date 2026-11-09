class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        # outline base cases
        memo[1] = 1
        memo[2] = 2
        def dynamic(x):
            # if x in memo, return it.
            if x in memo:
                return memo[x]
            
            # if n not in memo, solve it and put it in memo and return it.
            memo[x] = dynamic(x-1) + dynamic(x-2)
            return memo[x]
        
        return dynamic(n)