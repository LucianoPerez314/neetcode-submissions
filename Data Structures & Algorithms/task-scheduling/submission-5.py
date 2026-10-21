import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []

        freq = {}
        # build a frequency table mapping letter to frequency.
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1

        # build max_heap based on frequency
        for task, f in freq.items():
            heapq.heappush(max_heap, (-f, task))
        
        cooldown = []
        cycle = 0
        while len(max_heap) != 0 or len(cooldown) != 0:
            # get task with most frequency
            if len(max_heap) != 0:
                f, task = heapq.heappop(max_heap) 
                # only tasks not on cooldown in max_heap
                # put it on cooldown
                if -f > 1: # only tasks with duplicates needs a cooldown.
                    heapq.heappush(cooldown, (cycle + n, task))
                    freq[task] -= 1

            # check if anything in cooldown can be readded if the time to readd it matches the current cycle.
            while len(cooldown) != 0:
                time_off_c = cooldown[0][0]
                if time_off_c == cycle:
                    _, task = heapq.heappop(cooldown)
                    heapq.heappush(max_heap, (-freq[task], task))
                else:
                    break
            cycle += 1
        return cycle

            
            




            