"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort()
        prevEnd = intervals[0][1]
        for start, end in range(intervals[1:]):
            if prevEnd > start:
                return False
        return True