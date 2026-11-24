class Solution:
    def jump(self, nums: List[int]) -> int:
        # minimum nmber of jumps from start = 1 + min(minimum number of jumps from next possible jump destinations)
        memo = {}
        def dp(i):
            # memo
            if i in memo:
                return memo[i]

            # base cases
            if i >= len(nums) - 1:
                memo[i] = 0
                return memo[i]

            # recursive cases
            max_jump_len = nums[i]
            memo[i] = len(nums)
            for j in range(i+1, i + max_jump_len + 1):
                memo[i] = min(memo[i], 1 + dp(j))

            return memo[i]
        return dp(0) 