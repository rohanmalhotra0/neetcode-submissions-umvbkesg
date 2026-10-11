class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Find first nonnegative number
        pivot = 0
        while pivot < n and nums[pivot] < 0:
            pivot += 1

        l = pivot - 1
        r = pivot
        res = []

        while l >= 0 and r < n:
            if nums[l] ** 2 < nums[r] ** 2:
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1

        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1

        while r < n:
            res.append(nums[r] ** 2)
            r += 1

        return res