class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def dp(exp):
            if exp in memo:
                return memo[exp]

            if exp == 0:
                memo[exp] = 1
                return memo[exp]

            if exp == 1:
                memo[exp] = x
                return memo[exp]

            if exp > 0:
                if exp % 2 == 0:
                    memo[exp] = dp(exp // 2) * dp(exp // 2)
                else:
                    memo[exp] = dp(exp // 2) * dp(exp // 2 + 1)
                
                return memo[exp]
            else: 
                if exp % 2 == 0:
                        memo[exp] = 1 / (dp(-exp // 2) * dp(-exp // 2))
                else:
                    memo[exp] = 1 / (dp(-exp // 2) * dp(-exp // 2 + 1))
                return memo[exp]

        return dp(n)
        
        


