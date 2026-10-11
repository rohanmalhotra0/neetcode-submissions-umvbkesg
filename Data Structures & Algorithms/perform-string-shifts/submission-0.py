class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s1 = ""
        count = 1
        for a , b in shift:
            s1.append(s[a])
            s1.append(s[b])
            count += 1
        count += 1
        while len(s1) != len(s2):
            s1.append(s[count])
            count += 1 
        return s1
            