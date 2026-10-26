class Solution:
    def isHappy(self, n: int) -> bool:
        seen, curr = set(), helper(str(n))
        while curr not in seen and curr != 1:
            seen.add(curr)
            curr = helper(str(curr))
        return curr == 1

def helper(s):
    summ = 0
    for c in s:
        summ += (int(c)) ** 2
    return summ
