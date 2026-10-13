class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hash_set
        hash_set = set(nums)
        m = -1 * float('inf')
        l = len(nums)
        if l == 0:
            return 0
        for num in hash_set:
            if num - 1 not in hash_set:
                k = 1
                comparer = num
                while comparer + 1 in hash_set:
                    k += 1
                    comparer += 1
                if k > m:
                    m = k
                
            
        return m
                    


        


        