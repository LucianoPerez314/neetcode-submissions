class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # edge case: all negative arrays
        pos = False
        for num in nums:
            if num > 0:
                pos = True
                break

        if not pos:
            return max(nums)

        # greedy strategy
        # only pursue decisions at positive numbers. 
        memo = {}
        
        def dp(i):
            # memo
            if i in memo:
                return memo[i]

            # base case
            if i == 0:
                memo[i] = nums[i]
                return memo[i]

            # recursive case
            # Is it better to extend the subarray ending at k - 1, or start a brand-new subarray right here at nums[k]?
            memo[i] = max(dp(i-1) + nums[i], nums[i])
            return memo[i]


        return max([dp(i) for i in range(len(nums))])