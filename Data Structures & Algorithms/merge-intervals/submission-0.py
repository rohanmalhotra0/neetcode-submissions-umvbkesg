class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevStart, prevEnd = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if start <= prevEnd:
                # Overlap: extend the previous interval
                prevEnd = max(prevEnd, end)
            else:
                # No overlap: save the previous interval
                res.append([prevStart, prevEnd])
                prevStart, prevEnd = start, end

        # Append the final interval
        res.append([prevStart, prevEnd])

        return res