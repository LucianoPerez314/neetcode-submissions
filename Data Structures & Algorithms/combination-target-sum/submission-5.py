class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        # helper explores paths recursively (finding target give nums and track current path and sum of path along with it.)
        def helper(path, s, idx):
            # sum equals target means good path is found. Duplicates already accounted for.
            if s == target:
                res.append(path)
                return
            # sum being greater than target indicates dead end.
            if s > target:
                return 
            for i, num in enumerate(nums):
                # Forward only rule. Don't go back to add things we already added.
                if i >= idx:
                    helper(path + [num], s + num, i)
        
        helper([], 0, -1)
        return res
        


