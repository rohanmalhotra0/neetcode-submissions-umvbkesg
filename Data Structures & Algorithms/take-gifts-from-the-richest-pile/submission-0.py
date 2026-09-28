class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        count = 0 
        maxIdx = 0
        while count < k:
            for i in range(len(gifts)):
                if gifts[maxIdx] < gifts[i]:
                    maxIdx = i 
            gifts[maxIdx] = int(gifts[maxIdx] ** 1/2)
            count += 1
        

        return sum(gifts)