from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def twoSum(numsFromI: List[int], oldI: int):
            complements = set()

            for num in numsFromI:
                # oldI + num + need = 0
                need = -(oldI + num)

                if need in complements:
                    triplet = tuple(sorted([oldI, num, need]))

                    if triplet not in seen:
                        seen.add(triplet)
                        res.append(list(triplet))

                complements.add(num)

        for i in range(len(nums)):
            # IMPORTANT: start AFTER i so we don't reuse nums[i]
            twoSum(nums[i + 1:], nums[i])

        return res