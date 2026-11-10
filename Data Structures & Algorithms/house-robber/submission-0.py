class Solution:
    def rob(self, nums: List[int]) -> int:
        # index of memo is the maximum amount of money from robbing that subset of houses.
        memo = [-1] * len(nums)
        memo[0] = nums[0]
            

        for i in range(1, len(nums)):
            num = nums[i]
            if memo[i] != -1:
                continue
            x, y = 0, 0
            if i-2 >= 0:
                x = memo[i-2]
            
            if i-3 >= 0:
                y = memo[i-3]

            memo[i] = max(nums[i] + x, nums[i-1] + y)
        
        return max(memo)
