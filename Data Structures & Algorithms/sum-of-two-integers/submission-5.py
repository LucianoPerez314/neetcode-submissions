class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Sum of two integers by OR ing their bits
        res = 0
        carry_bit = 0
        for i in range(32):
            # extract ith bit from a and b
            a_bit = ((a >> i) & 1)
            b_bit = ((b >> i) & 1)
            if carry_bit == 0:
                if a_bit == 0 and b_bit == 0: #0 + 0 + 0 = 0
                    continue
                elif a_bit != b_bit: #0 + 1 + 0 = 1
                    res |= (1 << i)
                else: #1 + 1 + 0 = 10
                    carry_bit = 1
            else:
                if a_bit == 0 and b_bit == 0: #0 + 0 + 1 = 1
                    res |= (1 << i)
                    carry_bit = 0
                elif a_bit != b_bit: #0 + 1 + 1 = 10
                    carry_bit = 1
                else: #1 + 1 + 1 = 11
                    carry_bit = 1
                    res |= (1 << i)


                
                
            # if 1 , 0  or 0, 1 , make that ith bit in result 1.
            

            # if 1, 1 set next left bit to 1.
        # mask to 32 bits
        mask = 0xFFFFFFFF
        #res &= mask

        # convert from 32-bit two's complement to Python int
        if res & 0x80000000:  # if sign bit is 1
            res = ~(res ^ mask)  # two's complement → negative
            

        return res
        