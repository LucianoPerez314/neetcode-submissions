class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # largest pile = m
        # number of piles = n
        # max number of hours to finish = h
        m = max(piles)
        start, end = 1, m
        current = m 
        mid = (start + end) // 2
        while start <= end:
            #Check if mid satisfies the hours.
            res = helper(mid, piles, h)
            if res:
                current = mid
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return current

    
def helper(k, piles, h):
    total_hrs = 0
    for pile in piles:
        total_hrs += math.ceil(pile / k)
    return total_hrs <= h

        