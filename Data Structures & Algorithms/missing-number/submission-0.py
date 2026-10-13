class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s1 = set([0, n])
        # s2 = set(nums)
        # s2 - s1
        # We basically create a list where if it was present in nums,
        # then its a dup in the new one and if it was absent,
        # then it only appears once.
        # then we use solution to find non-duplicate
        n = len(nums)
        rnge = list(range(n+1))
        rnge = rnge + nums
        res = 0
        for num in rnge:
            res = res ^ num
        return res

    

            


        