class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)

        odd_count = 0

        for v in count.values():
            if v % 2 == 1:
                odd_count += 1

        return odd_count <= 1