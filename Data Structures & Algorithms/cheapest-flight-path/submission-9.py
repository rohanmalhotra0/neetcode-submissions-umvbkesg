class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = defaultdict(list)
        for u , v , cost in flights:
            m[u].append((v, cost))
        print(m)
        
        seen = set()
        seen.add(src)
        #q = deque((src, 0, 0))
        q = []
        heapq.heappush(q, (0, src, 0))
        while q:
            print(q)
            #  Current Cost, Node, X turns
            cost, node, x = heapq.heappop(q)
            
            if node == dst:
                return cost

            if x == k + 1:
                continue

            if cost > dist[(node, x)]:
                continue
            
            for nei , c in m[node]:
                if nei in seen:
                    continue
                heapq.heappush(q, (cost + c, nei, x + 1))
                seen.add(nei)
        return -1 

