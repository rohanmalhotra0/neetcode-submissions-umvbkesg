class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        if len(text1) > len(text2):
            s = text2
            a = text1
        else:
            s = text1
            a = text2
        res = 0
        m = defaultdict(str)
        curr = ""
        for c in s:
            curr += c
            m[curr] = len(curr)
        for c in a:
        """
        a=set(text1)
        b=set(text2)
        c = a & b
        return len(list(c))
         
