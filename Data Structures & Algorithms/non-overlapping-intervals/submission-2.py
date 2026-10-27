class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by end time.
        intervals.sort(key=lambda x: x[1])
        count = len(intervals)
        # greedy approach: 
        # Keep the interval that finishes earliest. 
        i = 0
        while i+1 < len(intervals):
            #print(intervals)
            o = overlap(intervals[i], intervals[i+1])
            # keep the interval that finished earliest. 
            if o:
                intervals.pop(i+1)
                continue
            i += 1
        return count - len(intervals)
        



def overlap(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if (start2 < start1 and start1 < end2):
        return True
    if (start1 < start2 and start2 < end1):
        return True
    if end1 == end2 or start1 == start2:
        return True
    return False
        
        



