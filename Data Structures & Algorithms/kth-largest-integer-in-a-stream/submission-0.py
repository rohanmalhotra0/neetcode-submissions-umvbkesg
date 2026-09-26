class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.kthElement = k
        self.nums = nums
        
        for i in range(len(nums)):
            self.nums[i] = -nums[i]
        heapq.heapify(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(-val)
        heapq.nlargest(self.kthElement)
        
        
