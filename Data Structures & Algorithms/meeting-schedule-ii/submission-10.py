"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        start, end = [x.start for x in intervals], [x.end for x in intervals]
        start.sort()
        end.sort()
        s, e = 0, 0
        count = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                s += 1
                continue
            s += 1
            e += 1
        return count


        

            

def overlapping(i1, i2):
    s1, e1 = i1.start, i1.end
    s2, e2 = i2.start, i2.end
    if s1 == s2 and e1 == e2:
        return True
    if s2 < s1 and s1 < e2:
        return True
    if s1 < s2 and s2 < e1:
        return True
    if s2 < e1 and e1 < e2:
        return True
    if s1 < e2 and e2 < e1:
        return True
    return False

def overlap(i1, i2):
    s1, e1 = i1.start, i1.end
    s2, e2 = i2.start, i2.end
    if s1 == s2 and e1 == e2:
        return i1
    if s2 < s1 and s1 < e2:
        if e1 < e2:
            return Interval(s2, e2)
        return Interval(s2, e1)
    if s1 < s2 and s2 < e1:
        if e1 < e2:
            return Interval(s1, e2)
        return Interval(s1, e1)
    return None