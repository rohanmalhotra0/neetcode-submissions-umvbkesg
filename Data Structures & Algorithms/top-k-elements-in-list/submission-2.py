class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums))]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for number, frequency in count.items():
            freq[frequency].append(number)
   
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for f in freq[i]:
                res.append(f)
                if k == len(res):
                    return res
                