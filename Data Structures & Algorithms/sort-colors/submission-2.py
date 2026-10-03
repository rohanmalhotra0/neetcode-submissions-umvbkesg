class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        for num in nums:
            freq[num] += 1
        for i in range(len(freq)):
            for j in range(i, freq[num]):
                nums[i] = freq[i]
                
                