class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_v = 0
        while l < r:
            v = min(heights[l], heights[r]) * (r - l)
            if v > max_v:
                max_v = v
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            
        return max_v
            

        
        
        

        