class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, -num))

        res = []

        while heap:
            freq, neg_num = heapq.heappop(heap)
            num = -neg_num

            for _ in range(freq):
                res.append(num)

        return res