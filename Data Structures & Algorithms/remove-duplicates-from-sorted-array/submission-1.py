class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        return len(seen)