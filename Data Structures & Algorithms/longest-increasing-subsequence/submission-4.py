class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        # 
        def dps(i):
            if i in memo:
                return memo[i]
            
            if i == len(nums)-1:
                memo[i] = 1
                return memo[i]
            # recursive case: 
            # longest increasing subsequence that must include nums[i] =
            # 1 + max of each longest increasing subequence at each element after i greater than nums[i] 
            incl = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    curr = 1 + dps(j)
                    incl = max(curr, incl)
            memo[i] = incl
            return memo[i]


        return max([dps(i) for i in range(len(nums))])
