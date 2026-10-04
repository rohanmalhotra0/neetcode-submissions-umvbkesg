class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        count = Counter(arr)
        for num in arr:
            if num + 1 in count and count[num+1] > 0:
                count[num+1] -= 1
                count += 1
        return count