class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        mid = -1
        while l < r:
            mid = (l + r + 1) // 2
            print(mid)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else: 
                break
        return mid