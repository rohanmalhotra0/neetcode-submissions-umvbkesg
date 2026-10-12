class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = defaultdict(list)
        for u , v , cost in flights:
            m[u].append((v, cost))
        
        seen = set(src)
        #q = deque((src, 0, 0))
        q = []
        q = heapq.heappush((0, src, 0))
        while q:
            # Node, Current Cost, X turns
            node, cost, x = heapq.heappop(q)
            if node == dst and x < k + 1:
                return cost
            if x > k:
                continue
            for nei , c in m[node]:
                if nei in seen:
                    continue
                heapq.heappush(q, (cost + c, nei, x + 1))
                seen.add(nei)
        return -1 

