class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo
        # solution = sum of solutions for nums excluding first number when we explore the first number as positive and negative.
        memo = {}
        def dp(i, s):
            # memo
            if (i, s) in memo:
                return memo[(i, s)]

            # base cases (at end of array)
            if i >= len(nums):
                if s == target:
                    memo[(i, s)] = 1
                    return memo[(i, s)]
                else:
                    memo[(i, s)] = 0
                    return memo[(i, s)]

            # recursive cases
            memo[(i, s)] = dp(i+1, s + nums[i]) + dp(i+1, s - nums[i])

            return memo[(i, s)]
        
        return dp(0, 0)