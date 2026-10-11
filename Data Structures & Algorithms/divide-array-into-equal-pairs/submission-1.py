class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if len(nums) % 2 == 1:
            return False
        for num , count in count.items():
            if count % 2 == 1:
                return False
        return True