class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        flag = False
        odd, even = False, False
        if len(s) % 2 == 0:
            even = True
        else:
            odd = True
        if odd:
            for v in count.values():
                if v % 2 == 1:
                    flag = True
                if v % 2 == 0:
                    continue
                else:
                    return False
            return True if flag else False
        if even:
            for v in count.values():
                if v == 1:
                    return False
                if v % 2 == 0:
                    continue
                else:
                    return False
            return True 