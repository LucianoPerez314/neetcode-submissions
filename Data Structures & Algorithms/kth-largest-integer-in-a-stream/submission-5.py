import heapq
class KthLargest:
    '''
    I guess the kth largest number sits at the top of a min heap as the root. 
    If a number smaller then the root sits at the top we ignore it. 
    If a number larger than the root comes along, we kick out the root and its next largest child becomes the new root. 
    And we insert the new number somehow.
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums[::]
        # Turn the initial list into a heap.
        heapq.heapify(self.minheap)
        # Limit the heap to only the upper end (kth-largest and larger elements) so we continually pop smaller elements.
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # edge case if minheap smaller than k
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            return self.minheap[0]
        if val <= self.minheap[0]: # if val is less than root we ignore it
            return self.minheap[0]
        else: 
            # If a number larger than the root comes along, we kick out the root. 
            # And we insert the new number somehow.
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
            return self.minheap[0]


        
    

