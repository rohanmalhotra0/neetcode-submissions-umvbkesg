from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            d = x ** 2 + y ** 2

            heapq.heappush(heap, (d, x, y))

        for i in range(k):
            d, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res