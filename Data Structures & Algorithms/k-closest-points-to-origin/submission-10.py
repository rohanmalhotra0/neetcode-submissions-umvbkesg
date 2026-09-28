from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return []
        res = []
        distance = {}
        dist = []
        for i in range(len(points)):
            d = sqrt(((points[i][0]^2) + (points[i][1]^2)))
            d = -d
            dist.append(d)
            distance[d] = [points[i][0], points[i][1]]  
        heapq.heapify(dist)
        for i in range(k):
            val = heapq.heappop(dist)
            x , y = distance[val]
            res.append([x,y])
        return res
