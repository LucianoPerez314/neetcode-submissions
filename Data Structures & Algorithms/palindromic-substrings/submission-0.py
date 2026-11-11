class Solution:
    def countSubstrings(self, s: str) -> int:
        # key = index, value = longest palindromic substring when treating that index as the center. 
        count = 0
        for i, c in enumerate(s):
            # odd length
            l, r = i, i
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # even length
            l, r = i, i+1
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count