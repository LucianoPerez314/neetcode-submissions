import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [] 

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            largest1 = -heapq.heappop(max_heap)
            largest2 = -heapq.heappop(max_heap)

            # If x == y, both stones are destroyed
            if largest1 == largest2:
                continue
            else:
                heapq.heappush(max_heap, -(largest1-largest2))

        if len(max_heap) == 0:
            return 0
        
        return -max_heap[0]
        