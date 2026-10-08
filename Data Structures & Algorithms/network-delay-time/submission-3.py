class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u , v , w in times:
            edges[u].append((v, w))
        minHeap = [(0, k)] # Weights , Start Node
        t = 0 # Min Total Cost
        visit = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in edges[u]:
                if n2 not in visit:
                    visit.add(n2)
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t