class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        # dc(amount) = sum_{i}(dc(amount - coins[i]))
        def combos(amt, i):
            # Memo
            if (amt, i) in memo:
                return memo[(amt, i)]

            # Base Cases
            if amt < 0 or i >= len(coins):
                memo[(amt, i)] = 0
                return memo[(amt, i)]

            if amt == 0:
                memo[(amt, i)] = 1
                return memo[(amt, i)]
            
            # Recursive cases
            # We account for combinations by never looking at small denominations only current denominations or more.
            # Choices are choose coin of denomination coin[i], or not and move onto coin of next denomination coin[i+1]
            memo[(amt, i)] = combos(amt - coins[i], i) + combos(amt, i+1)
            return memo[(amt, i)]
        
        return combos(amount, 0)

            