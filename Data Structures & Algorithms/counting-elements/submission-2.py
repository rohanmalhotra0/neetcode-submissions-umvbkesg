class Solution:
    def countElements(self, arr: List[int]) -> int:
        counts = 0
        count = Counter(arr)
        for num in arr:
            if num + 1 in count and count[num+1] > 0:
                count[num+1] -= 1
                counts += 1
        return counts