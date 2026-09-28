class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                count +=1
        return count
        