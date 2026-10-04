class Solution:
    def largestGoodInteger(self, num: str) -> str:
        window  = num[0:3]
        maxVal = 0

        for i in range(3, len(num)-3):
            
            if len(set(window)) == 1:
                maxVal = max(int(window[0]), maxVal)
            window = num[i-2:i]
        maxStr = str(maxVal) + str(maxVal) + str(maxVal)
        
        return maxStr if maxVal != 0 else ''
        