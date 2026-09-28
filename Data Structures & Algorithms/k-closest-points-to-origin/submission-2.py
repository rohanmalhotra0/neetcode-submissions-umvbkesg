from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return []

        distance = {}
        dist = []
        for i in range(len(points)):
            dist = -sqrt((points[i][0])^2 + (points[i][1]^2))
            distance[dist] = [points[i][0], points[i][1]]  
        heapq.heapify(dist)
        for i in range(k):
            x , y = heapq.heappop(dist)
            res.append([x,y])
        
