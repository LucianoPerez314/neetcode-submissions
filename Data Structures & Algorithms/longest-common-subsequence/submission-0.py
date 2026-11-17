class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        # lcs of text1 starting at i and text2 starting at j =  
        # if first char matches: lcs(i, j) = 1 + lcs(i+1, j+1)
        # if first char doesn't match: lcs(i, j) = max(lcs(i+1, j), lcs(i, j+1)) 
        def lcs(i, j):
            # Memo
            if (i, j) in memo:
                return memo[(i, j)]

            # Base cases
            if i == len(text1) or j == len(text2):
                memo[(i, j)] = 0
                return 0

            # Recursive cases
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs(i+1, j+1)
                return memo[(i, j)]

            memo[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))
            return memo[(i, j)]
            
        return lcs(0, 0)
        