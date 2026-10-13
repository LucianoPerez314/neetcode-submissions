class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #map<character, most recent occurence index>
        r = 0
        sub_s = dict()
        longest = 0
        while r < len(s):
            #if queue is empty or the characters do not equal
            if not sub_s or s[r] not in sub_s:
                sub_s[s[r]] = r
            #the is not empty and the characters equal
            else:
                r = sub_s[s[r]] + 1
                sub_s = {s[r]: r}
            longest = max(longest, len(sub_s))
            r += 1
        return longest



                
            

        