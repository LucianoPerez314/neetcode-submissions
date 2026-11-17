class Solution:
    def reverse(self, x: int) -> int:
        res = int(0)

        neg = x < 0
        x = abs(x)

        while x > 0:
            res = res * 10
            digit = x % 10      # Extract the rightmost digit (9, then 2, then 8, then 4)
            res += digit
            x = x // 10
        
        if neg:
            if -res < (-2 ** 31) - 1:
                return 0
            return -res
        
        if res > (2 ** 31) - 1:
            return 0
        return res