class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = dict()
        for char in s:
            if char not in sHash:
                sHash[char] = 1
            else:
                sHash[char] += 1
        
        for char in t:
            if char not in sHash:
                return False
            else:
                sHash[char] -= 1

        for key in sHash:
            if sHash[key] != 0:
                return False
        return True


        