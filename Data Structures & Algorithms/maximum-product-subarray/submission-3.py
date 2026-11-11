class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curr_min = 1
        curr_max = 1

        for n in nums:
            tmp = curr_max * n 
            curr_max = max(tmp, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)
            res = max(res, curr_max, curr_min)
        return res
        


        