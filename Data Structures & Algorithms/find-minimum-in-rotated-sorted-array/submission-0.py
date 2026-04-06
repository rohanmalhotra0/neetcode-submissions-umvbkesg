class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minf = nums[0]

        while l <= r:
            m = (l + r) // 2
            minf = min(minf, nums[m])

            # compare middle to right
            if nums[m] > nums[r]:
                l = m + 1      # min is in right half
            else:
                r = m - 1      # min is in left half (including m)

        return minf