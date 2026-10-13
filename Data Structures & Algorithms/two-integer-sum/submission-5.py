class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, n in enumerate(nums):
            d[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in d and d[diff] != i:
                sol = [i, d[diff]]
                return [min(sol), max(sol)]



        


            





        