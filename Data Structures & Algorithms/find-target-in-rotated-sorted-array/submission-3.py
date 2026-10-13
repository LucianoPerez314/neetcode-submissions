class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # If subarray properly sorted.
            if nums[l] < nums[r]:
                # perform normal binary search
                if target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # l = m + 1
            # r = m - 1
            if nums[m] >= nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
              
        return -1