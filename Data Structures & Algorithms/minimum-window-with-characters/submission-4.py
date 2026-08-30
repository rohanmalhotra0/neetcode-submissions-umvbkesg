class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t or not s:
            return ""

        countT = [0] * 128

        for ch in t:
            countT[ord(ch)] += 1

        window = [0] * 128

        l = 0
        have = 0
        need = len(t)

        minStr = ""
        minLen = float("inf")

        for r in range(len(s)):
            window[ord(s[r])] += 1

            # did this new character satisfy one needed occurrence?
            if window[ord(s[r])] <= countT[ord(s[r])]:
                have += 1

            # window now contains all chars of t
            while have == need:

                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minStr = s[l:r + 1]

                # remove left character
                window[ord(s[l])] -= 1

                # did removing it make the window invalid?
                if window[ord(s[l])] < countT[ord(s[l])]:
                    have -= 1

                l += 1

        return minStr