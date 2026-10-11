class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1 
        for i in range(len(arr)):
            if count[i] == i - 1 and count[i] != 0:
                res = i 
        return res 
                