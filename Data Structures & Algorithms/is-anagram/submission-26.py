class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] = 1 + count.get(c, 0)
        for c in t:
            count[c] -= 1 
 
        
        return all(value == 0 for value in count.values())
        
