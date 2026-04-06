class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if len(s) != len(t):
            return False
        set1 = set()
        set2 = set()
        for letter1, letter2 in zip (s, t):
            set1.add(letter1)
            set2.add(letter2)
        return set1 == set2
        '''
        
    
        s1 = sorted(s)
        t1 = sorted(t)
        if s1 == t1:
            return True
        else:
            return False

