class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ex: if 3 is seen mark arr[2] as negative
        for i, n in enumerate(nums):
            if n < 0:
                n = n * -1
            # If nums[n-1] at i is negative we marked it already and 
            # i+1 is the dup
            if nums[n-1] < 0:
                return n
            else:
                nums[n-1] = nums[n-1] * -1


