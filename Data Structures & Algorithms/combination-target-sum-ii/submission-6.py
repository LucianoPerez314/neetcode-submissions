class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates_s = list(sorted(candidates))
        # helper explores paths recursively (finding target give nums and track current path and sum of path along with it.)
        def helper(path, s, idx):
            # print(path, idxs)
            # sum equals target means good path is found. Duplicates already accounted for.
            if s == target:
                res.append(path)
                return
            # sum being greater than target indicates dead end.
            if s > target:
                return 
            for i in range(idx+1, len(candidates_s)):
                # Forward only rule. Don't go back to add things we already added.
                if i > idx:
                    if i == idx + 1 or candidates_s[i] != candidates_s[i - 1]:
                        num = candidates_s[i]
                        helper(path + [num], s + num, i)
        
        helper([], 0, -1)
        return res