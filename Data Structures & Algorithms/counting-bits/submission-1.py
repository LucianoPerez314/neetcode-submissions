class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            res = 0
            while i:
                # This adds 1 to result if rightmost bit is 1.
                res += i % 2
                # This shifts the bits rightward by 1.
                i  =  i >> 1
            lst.append(res)

        return lst

        