"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        i = 0
        while i+1 < len(intervals):
            if overlapping(intervals[i], intervals[i+1]):
                return False
            i += 1
        return True


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