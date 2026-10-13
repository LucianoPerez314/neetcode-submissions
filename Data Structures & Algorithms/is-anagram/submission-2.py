class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        ds, dt = dict(), dict()
        if ls != lt:
            return False
        

        for i in range(ls):
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] = ds[s[i]] + 1

        for i in range(ls):
            if t[i] not in dt:
                dt[t[i]] = 1
            else:
                dt[t[i]] = dt[t[i]] + 1
    
        
        return ds == dt
            

        



        