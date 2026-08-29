class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def permute(s):
            if len(s) == 1:
                return [s]
            
            permutations = []
            for i, char in enumerate(s):
                remaining = s[:i] + s[i+1:]

                for p in permute(remaining):
                    permutations.append(char + p)

            return permutations

        permutations = permute(s1)

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if s2[l:r + 1] in permutations:
                return True

            l += 1
            r += 1

        return False
            