class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: 
            x *= -1 
            s = str(x)
            l, r = 0 , len(s) -1 
            while l < r: 
                s[l], s[r] = s[r] , s[l]
                l += 1
                r -= 1
            return int(s)
        else:
            s = str(x)
            l, r = 0 , len(s) -1 
            while l < r: 
                s[l], s[r] = s[r] , s[l]
                l += 1
                r -= 1
            return int(s)