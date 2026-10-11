class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s1 = ""
        count = 1
        for a , b in shift:
            s1 += s[b]
            s1 += s[a]
            count += 1
      
        while len(s1) != len(s):
            s1 += s[count]
            count += 1 
        return s1
            