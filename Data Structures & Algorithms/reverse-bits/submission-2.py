class Solution:
    def reverseBits(self, n: int) -> int:
        # n -> 2*n - 1
        # bit-shift?
        # 0 -> 31
        # 1 -> 30
        # 2 -> 29
        res = 0
        for i in range(32):
            
            # extract the bit at i 
            bit = ((n >> i) & 1) # this moves the ith bit to the right by i so it is
            # at 0, then we do bit & 1 to extract the bit.
            # if the bit is 1 we shift it.
            if bit == 1:
                # move position i to position 31 - i
                res |= (1 << (31 - i))

        return res

        