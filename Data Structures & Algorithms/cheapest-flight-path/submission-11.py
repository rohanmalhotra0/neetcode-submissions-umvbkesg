from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)

        for u, v, cost in flights:
            adj[u].append((v, cost))

        dist = defaultdict(lambda: float("inf"))
        dist[(src, 0)] = 0

        heap = [(0, src, 0)]

        while heap:
            cost, node, x = heapq.heappop(heap)

            if node == dst:
                return cost

           
            if x == k + 1:
                continue

            for nei, weight in adj[node]:
                newCost = cost + weight
                state = (nei, x + 1)

                if newCost < dist[state]:
                    dist[state] = newCost
                    heapq.heappush(heap, (newCost, nei, x + 1))

        return -1