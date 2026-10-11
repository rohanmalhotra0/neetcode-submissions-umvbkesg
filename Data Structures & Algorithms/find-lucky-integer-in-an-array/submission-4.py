class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1 
        for num in count:
            if num == count[num]:
                res = max(num, res)

        return res