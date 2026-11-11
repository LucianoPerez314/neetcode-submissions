class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()
        def dp(sub):
            if sub in memo:
                return memo[sub]
            # Base case
            # Empty substring
            if len(sub) == 0:
                memo[sub] = 1
                return memo[sub]

            # One character 
            if len(sub) == 1:
                if sub != '0':
                    memo[sub] = 1
                    return memo[sub]
                memo[sub] = 0
                return memo[sub]


            # Recursive case
            # Split at first.
            count = 0
            if sub[0] != '0':
                # print(sub, sub[1:])
                count += dp(sub[1:])

            # Split at second.
            if 10 <= int(sub[:2]) <= 26:
                count += dp(sub[2:])
            memo[sub] = count
            return memo[sub]
            

        return dp(s)
            