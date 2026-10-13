class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dump = set()
        for num in nums:
            if num in dump:
                return True
            dump.add(num)
        return False
        