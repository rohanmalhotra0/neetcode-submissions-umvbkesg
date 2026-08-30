class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.replace("'", "")
        s = s.replace(":", "")

        l = 0
        r = len(s) - 1 
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1 
        return True