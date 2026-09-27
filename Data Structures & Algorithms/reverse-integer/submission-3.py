class Solution:
    def reverse(self, x: int) -> int:
        # Remember whether x is negative
        sign = -1 if x < 0 else 1

        # Convert absolute value into a list
        s = list(str(abs(x)))

        # Reverse using two pointers
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        # Join characters and restore the sign
        res = sign * int("".join(s))

        # Check 32-bit integer bounds
        if res < -(2**31) or res > 2**31 - 1:
            return 0

        return res
