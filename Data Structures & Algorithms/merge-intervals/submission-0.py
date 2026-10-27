class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by start time.
        intervals.sort()

        i = 0
        while i+1 < len(intervals):
            o = overlap(intervals[i], intervals[i+1])

            if o:
                intervals[i] = o
                intervals.pop(i+1)
                continue
            i += 1
        return intervals




def overlap(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    if (start2 <= start1 and start1 <= end2):
        if end1 <= end2:
            #print(2, 2)
            return [start2, end2]
        #print(2, 1)
        return [start2, end1]
    if (start1 <= start2 and start2 <= end1):
        if end1 <= end2:
            #print(1, 2)
            return [start1, end2]
        #print(1, 1)
        return [start1, end1]
    
    return []