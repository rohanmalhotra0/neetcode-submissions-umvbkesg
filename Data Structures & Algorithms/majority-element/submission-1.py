from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = Counter(nums)
        return max(x)