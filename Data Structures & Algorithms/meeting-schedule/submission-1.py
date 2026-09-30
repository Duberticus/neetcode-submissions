"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda k : k.start)

        for i in range(1, len(intervals)):
            first = intervals[i-1]
            toCMP = intervals[i]

            if first.end > toCMP.start:
                return False
        return True
