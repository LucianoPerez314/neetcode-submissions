class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                return True
        return False

         