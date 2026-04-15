class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.sort()
        s1 = s1.lower()
        s1 = s1.replace("", " ")
        for i in range(1, len(s)):
            if (s1[i] != s1(i-1)):
                return False
        return True