class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            b = bin(i)[2:]
            b = [int(c) for c in b]
            lst.append(sum(b))

        return lst

        