class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            anchor = nums[i]
            # get the permutations of everything excluding the current element.
            sub_perms = self.permute(nums[:i] + nums[i+1:])
            # add the current element at between every element in the permutations.
            for perm in sub_perms:
                res.append([anchor] + perm)
        return res