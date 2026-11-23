class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        final = 0 
        for i in range(len(num1)-1, -1, -1): # bottom number
            c1 = num1[i]
            place1 = len(num1) - i
            carry = 0
            for j in range(len(num2)-1, -1, -1): # top number
                place2 = len(num2) - j
                c2 = num2[j]
                product = mult(c1, c2)
                res = product + carry
                carry = res // 10
                final += (res % 10) * (10 ** (place1 + place2 - 2))
            
            if carry != 0:
                final += carry * (10 ** (place1 + len(num2) - 1))

        return str(final)


def add(c1, c2):
    d1 = ord(c1) - ord('0')
    d2 = ord(c2) - ord('0')

    raw = d1 + d2
    carry = (d1 + d2) // 10
    curr = (d1 + d2) % 10 
    return (raw, carry, curr)

def mult(c1, c2):
    d1 = ord(c1) - ord('0')
    d2 = ord(c2) - ord('0')

    raw = d1 * d2
    return raw
