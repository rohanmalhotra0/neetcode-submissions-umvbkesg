class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s = 0
        e = 0
        res = 0
        rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                # Meeting starts before another ends
                rooms += 1
                s += 1
            else:
                # A meeting has ended; free its room
                rooms -= 1
                e += 1

            res = max(res, rooms)

        return res