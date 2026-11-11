class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dp Approach
        # key is amount, value is minimum number of coins needed to satisfy it. 
        memo = dict()
        def dp(a):
            # Base cases
            if a < 0: # Negative amount, impossible
                return float('inf')
            
            if a == 0: # No amount, no coins needed.
                return 0
            
            if a in memo:
                return memo[a]
            # Recursive case
            min_coins = float('inf')
            for i, coin in enumerate(coins): # pick a coin
                # solve sub-problem where the amount has the picked coin subtracted from it.
                # add 1 since we picked a coin
                min_coins = min(min_coins, 1 + dp(a - coin))

            memo[a] = min_coins
            return memo[a]

        res = dp(amount)
        if res == float('inf'):
            res = -1
        return res