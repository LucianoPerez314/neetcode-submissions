class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # solution of can jump starting at first element = solution of can jump starting at elements jumped to from first element.
        # we prune options where the jump length is 0 inluess its the last index since these are dead ends.
        memo = {}
        def dp(i):
            # memo
            if i in memo:
                return memo[i]

            # base case:
            if i >= len(nums) - 1:
                memo[i] = True
                return memo[i]
            
            
            # recursive case
            memo[i] = False
            jump_len = nums[i]
            for j in range(i+1, i + jump_len + 1):
                if j >= len(nums) - 1:
                    memo[i] = dp(j)
                elif j < len(nums) and nums[j] != 0 and dp(j):
                    memo[i] = True
                    break

            return memo[i]

        return dp(0)
        