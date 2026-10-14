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
            # Forward only rule. Don't go back to add things we already added. That's why we start at idx+1. 
            # Think of idx as a checkpoint.
            for i in range(idx+1, len(candidates_s)):
                # Prevents pursuing a branch if the previous branch is already pursued.
                '''
                The extra check (candidates_s[i] != candidates_s[i - 1]) tells the algorithm: 
                "Hey, we already explored what happens when we start a branch with this number at this level. 
                Don't waste time doing it again with the identical twin right next to it."
                '''
                if i == idx + 1 or candidates_s[i] != candidates_s[i - 1]:
                    num = candidates_s[i]
                    helper(path + [num], s + num, i)
        
        helper([], 0, -1)
        return res