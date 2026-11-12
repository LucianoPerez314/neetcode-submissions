class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Sort the keys in decreasing order (greedy approach)
        wordDict.sort(key=len, reverse=True)
        # key is index for start of substring, value is true or false if that substring can be broken into worddict words. 
        memo = dict()
        def dp(i):
            # Base Case: Solution is already found for substring
            if i in memo:
                return memo[i]

            # Base Case: string is empty (we've broken off every word from s)
            if len(s) == i:
                memo[i] = True
                return memo[i]
            
            # Recursive case: 
            # break off all the words at the start of the string.
            # explore subproblem for each of these individual cases. 
            res = False
            for word in wordDict:
                # print(i, len(word), word, s[i:len(word)+i], len(word) <= len(s) - i, word == s[i:len(word)+i])
                if len(word) <= len(s) - i and word == s[i:len(word)+i] and dp(len(word)+i):
                    res = True
                    break
            
            memo[i] = res
            return memo[i]
        return dp(0)




        


        