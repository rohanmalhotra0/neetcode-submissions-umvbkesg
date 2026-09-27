class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range (len(digits)):
            s.append(str(digits[i]))
        x = int(s)
        x +=1 
        x = list(str(x))
        return x
