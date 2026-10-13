class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixs = []
        suffixs = []
        for i in range(l):
            prefix = 1
            for j in range(i):
                prefix = prefix * nums[j]
            prefixs.append(prefix)
        
        for i in range(l):
            suffix = 1
            for j in range(i+1,l):
                suffix = suffix * nums[j]
            suffixs.append(suffix)
        res = []
        for i in range(l):
            res.append(prefixs[i] * suffixs[i])
        return res


        

            


            
        