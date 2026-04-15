class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        res {}
        for s in str:
           count = [26] * 0
           for c in s:
               count[ord(c)- ord("a")] += 1
            res[count].append(s)
         return res.values()
         '''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[count].append(s)
        return list(res.values())


         