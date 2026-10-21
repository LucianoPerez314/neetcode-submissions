class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        # add 1 to rightmost digit.
        if digits[-1] + 1 > 9:
            carry = 1
            digits[-1] = 0
        else:
            digits[-1] += 1
            return digits

        # propagate carry over.
        for i in range(len(digits)-2, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        res = [1] + digits
        return res
        



        