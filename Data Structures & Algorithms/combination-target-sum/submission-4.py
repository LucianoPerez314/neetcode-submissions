class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        # helper explores paths recursively (finding target give nums and track current path along with it.)
        def helper(path, s, idx):
            # path_id is to prevent adding duplicates to res
            if s == target:
                res.append(path)
                return
            if s > target:
                return 
            for i, num in enumerate(nums):
                # Forward only rule.
                if i >= idx:
                    helper(path + [num], s + num, i)
        
        helper([], 0, -1)
        return res
        


