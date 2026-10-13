class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If subarray properly sorted.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            # Check if the middle is greater than the start
            if nums[m] >= nums[l]: # middle > start and start > end
                # thus the bigger subarray is the left subarray
                # Minimum is in the right array
                l = m + 1
            else: # middle < start and start > end
                # thus the bigger subarray is the right subarray
                # Minimum is in the left array
                r = m - 1
        return res



        

        