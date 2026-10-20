import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []
        # treat distance as the priority in the priority queue.
        for point in points:
            x, y = point[0], point[1]
            d = dist(0, 0, x, y)
            heapq.heappush(min_heap, (d, point))
        
        for _ in range(k):
            d, point = heapq.heappop(min_heap)
            res.append(point)
        return res


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)