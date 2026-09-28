class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums2 + nums1
        for i in range(len(nums3)):
            if i < len(nums1) or nums1[i] != 0:
                nums1[i] = nums3[i]

