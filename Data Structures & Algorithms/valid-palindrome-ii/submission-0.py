class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = Counter(s)

        if len(s) % 2 == 0:
            x = 0
            for key, val in count.items():
                if val == 1:
                    x +=1
            return False if x > 1 else True
        else:
            x = 0
            for key, val in count.items():
                if val == 1:
                    x +=1
                return False if x > 2 else True    
    
