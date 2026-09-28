class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        return len(seen)