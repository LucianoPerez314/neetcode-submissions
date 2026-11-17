class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        # mp(haveCoin, i) = 
        # if haveCoin
        def mp(haveCoin, i):
            # Memo
            if (haveCoin, i) in memo:
                return memo[(haveCoin, i)]

            # Base cases
            if i >= len(prices):
                return 0

            # Recursive cases
            # If you have a neetcoin, the choice is selling it or not selling it.
            if haveCoin:
                # If you sell it then you don't have a choice the next day so you skip a day.
                memo[(haveCoin, i)] = max(mp(True, i+1), mp(False, i+2) + prices[i])
                return memo[(haveCoin, i)]
            
            # If you don't have a neetcoin. Your choice is buying or not buying it.
            memo[(haveCoin, i)] = max(mp(True, i+1) - prices[i], mp(False, i+1))
            return memo[(haveCoin, i)]
            

        return mp(False, 0)




            