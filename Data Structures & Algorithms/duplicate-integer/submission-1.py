class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for num in nums:
            if num not in dic:
                dic.add(num)
            else:
                return True
        return False

         