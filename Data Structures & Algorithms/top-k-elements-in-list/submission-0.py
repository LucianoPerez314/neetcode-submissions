class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        v = list(dic.values())
        keys = list(dic.keys())
        res = []
        while k > 0:
            max_val = max(v)
            max_k = keys[v.index(max_val)]
            res.append(max_k)
            v.remove(max_val)
            keys.remove(max_k)
            k -= 1
        return res
        