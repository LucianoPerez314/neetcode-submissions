class Solution:
    def longestPalindrome(self, s: str) -> str:
        # key = index, value = longest palindromic substring when treating that index as the center. 
        longest = ''
        ll = 0
        for i, c in enumerate(s):
            # odd length
            l, r = i, i
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                if r - l + 1 > ll:
                    longest = s[l:r+1]
                    ll = (r - l) + 1
                l -= 1
                r += 1
            # even length
            l, r = i, i+1
            while 0 <= l and r <= len(s)-1 and s[l] == s[r]:
                if r - l + 1 > ll:
                    longest = s[l:r+1]
                    ll = (r - l) + 1
                l -= 1
                r += 1
        return longest



        