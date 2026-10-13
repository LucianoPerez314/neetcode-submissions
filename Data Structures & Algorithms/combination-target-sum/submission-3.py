class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = {}
        def helper(path, s, idx):
            path_id = str(sorted(path))
            if s == target and path_id not in res:
                res[path_id] = path
                return
            if s > target:
                return 
            for i, num in enumerate(nums):
                if i >= idx:
                    helper(path + [num], s + num, i)
        
        helper([], 0, -1)
        return list(res.values())
        


