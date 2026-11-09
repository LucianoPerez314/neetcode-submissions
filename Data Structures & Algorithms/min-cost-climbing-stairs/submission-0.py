class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # key is floor index, value is the minimum cost from the start to this current floor index
        memo = defaultdict(int)
        # outline base cases
        memo[0] = 0
        memo[1] = 0
        def dynamic(x):
            # if x in memo, return it.
            if x in memo:
                return memo[x]
            
            # if n not in memo, solve it and put it in memo and return it.
            memo[x] = min(dynamic(x-1)+cost[x-1], dynamic(x-2)+cost[x-2])
            return memo[x]
        
        return dynamic(len(cost))