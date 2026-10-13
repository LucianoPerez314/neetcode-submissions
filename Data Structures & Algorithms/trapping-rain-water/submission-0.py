class Solution:
    def trap(self, height: List[int]) -> int:
        max_level = max(height)
        #level-by-level?
        #consider only numbers at level 1.
        #then consider numbers at level 2.
        curr_level = 1
        total_vol = 0
        while curr_level < max_level + 1:
            nums = []
            for num in height:
                if num < curr_level:
                    nums.append(0)
                if num >= curr_level:
                    nums.append(1)
            total_vol += self.vol_by_level(nums)
            curr_level += 1
        return total_vol
            
    
    def vol_by_level(self, nums):
        l = 0
        r = len(nums) - 1
        count = 0
        while nums[l] != 1 and l < r:
            l += 1
        
        while nums[r] != 1 and r > l:
            r -= 1

        while l < r:
            if nums[l] == 0:
                count += 1
            l += 1

            
        return count
            

