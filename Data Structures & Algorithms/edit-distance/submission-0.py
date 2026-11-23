class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # min distance word1, word2 = 
        # min distance of word1[i:], word2[j:] plus edits to make word[:i] and word[:j] match
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # base case
            if i >= len(word1) and j >= len(word2):
                memo[(i, j)] = 0
                return memo[(i, j)]
            
            if i >= len(word1):
                memo[(i, j)] = len(word2) - j
                return  memo[(i, j)]
            
            if j >= len(word2):
                memo[(i, j)] = len(word1) - i
                return  memo[(i, j)]


            # recursive cases

            # letter matches
            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                memo[(i, j)] = dp(i+1, j+1)
                return memo[(i, j)]

            if i < len(word1) and j < len(word2) and word1[i] != word2[j]:
                # replace character
                res1 = dp(i+1, j+1)
                # delete character
                res2 = dp(i+1, j)
                # add character
                res3 = dp(i, j+1)
                memo[(i, j)] = 1 + min(res1, res2, res3)
                return memo[(i, j)]
        return dp(0, 0)