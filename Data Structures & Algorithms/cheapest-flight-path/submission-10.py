from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        m = defaultdict(list)

        for u, v, cost in flights:
            m[u].append((v, cost))

        q = [(0, src, 0)]

        # (node, flights_used) -> cheapest cost
        dist = {(src, 0): 0}

        while q:
            cost, node, x = heapq.heappop(q)

            if node == dst:
                return cost

            if x == k + 1:
                continue

            if cost > dist[(node, x)]:
                continue

            for nei, c in m[node]:
                newCost = cost + c
                state = (nei, x + 1)

                if newCost < dist.get(state, float("inf")):
                    dist[state] = newCost
                    heapq.heappush(q, (newCost, nei, x + 1))

        return -1