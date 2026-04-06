class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.replace("'", "")
        s = s.replace(".", "")
        s = s.lower()
        R = len(s) - 1
        print(s)
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True 