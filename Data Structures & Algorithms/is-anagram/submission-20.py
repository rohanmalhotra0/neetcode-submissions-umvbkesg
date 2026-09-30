class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1 + count.get(c, 0)
        for c in t:
            count[c] -= 1 
        print(count)
        return True if max(count.values()) == 0 else False
        
