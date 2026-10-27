class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        while i < len(intervals):
            # find nearest start interval (check by start of each interval)
            if not intervals[i][1] < newInterval[0]:
                break
            i += 1
        print("I", i)
        if i >= len(intervals):
            intervals.insert(i, newInterval)
            return intervals

        print("C1", intervals[i])
        o = overlap(intervals[i], newInterval)
        print("O1", o)
        if o:
            intervals[i] = o
        else:
            intervals.insert(i, newInterval)
            return intervals

        # merge intervals overlapping with start interval
        while i+1 < len(intervals):
            o = overlap(intervals[i], intervals[i+1])
            if o:
                intervals[i] = o
                intervals.pop(i+1)
            else:
                break
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
