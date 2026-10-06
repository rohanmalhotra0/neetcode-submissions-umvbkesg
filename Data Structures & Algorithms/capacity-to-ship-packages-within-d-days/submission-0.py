class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = 1, max(weights)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in weights:
                totalTime += (p + k - 1) // k
            if totalTime <= days:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res