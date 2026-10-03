class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large , num)
        else:
            heapq.heappush(self.small , num)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small , -1 * val)
        


       
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * heapq.heappop(self.small)
        elif len(self.small) < len(self.large):
            return heapq.heappop(self.large)
        else:
            return  (-1 * heapq.heappop(self.small) + heapq.heappop(self.large)) // 2

      