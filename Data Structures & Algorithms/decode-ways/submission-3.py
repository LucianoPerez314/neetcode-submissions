class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()
        def dp(sub):
            if sub in memo:
                return memo[sub]
            # Base case
            # Empty substring. We ended up on a good path.
            if len(sub) == 0:
                memo[sub] = 1
                return memo[sub]

            # One character. Good path if char is valid bad path if a lone 0 is here. 
            if len(sub) == 1:
                if sub != '0':
                    memo[sub] = 1
                    return memo[sub]
                memo[sub] = 0
                return memo[sub]


            # Recursive case
            # Split at first.
            count = 0
            if sub[0] != '0': # If first char is valid we are on a good path and continue down it. 
                # print(sub, sub[1:])
                count += dp(sub[1:])

            # Split at second.
            if 10 <= int(sub[:2]) <= 26: # If two digits are valid we are on a good path so we continue down it.
                count += dp(sub[2:])
            memo[sub] = count
            return memo[sub]
            

        return dp(s)
            