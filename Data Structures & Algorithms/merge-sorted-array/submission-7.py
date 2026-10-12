class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_copy = nums1[:m]
        r = 0
        i = j = 0
        while r < m + n:
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[r] = nums1_copy[i]
                i += 1
            else:
                nums1[r] = nums2[j]
                j += 1
            idx += 1