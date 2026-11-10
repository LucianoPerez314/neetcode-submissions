class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # index of memo is the maximum amount of money from robbing that subset of houses.
        
        memo = [-1] * len(nums)
            
        first = nums[:-1]
        second = nums[1:]

        def dfs(i, arr, mem):
            if i < 0 or len(arr)-1 < i:
                return 0
            if mem[i] != -1:
                return mem[i]
            
            mem[i] = max(arr[i] + dfs(i+2, arr, mem), dfs(i+1, arr, mem))
            return mem[i]
        return max(dfs(0, first, memo[::]), dfs(0, second, memo[::]))


