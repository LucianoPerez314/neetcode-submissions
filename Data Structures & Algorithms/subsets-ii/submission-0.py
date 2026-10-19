class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            # base case (we have a raw subset)
            if i == len(nums):
                res.append(subset[::])
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            # All subsets that don't include nums[i] (duplicates of nums[i] are considered nums[i])
            subset.pop()
            # iterate to next unique num.
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res