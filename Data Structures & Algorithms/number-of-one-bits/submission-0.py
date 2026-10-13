class Solution:
    def hammingWeight(self, n: int) -> int:
        # 4
        # 2 ld 4 = 2 remainder 0
        # 2 ld 2 = 1 remainder 0
        # 2 ld 1 = 0 remainder 1
        b = bin(n)[2:]
        print(b)         
        b = [int(i) for i in b]
        return sum(b)