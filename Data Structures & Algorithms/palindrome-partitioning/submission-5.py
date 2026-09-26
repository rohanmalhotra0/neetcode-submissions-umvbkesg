class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        
        def dfs(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.isPal(s, i ,j):
                    cur.append(s[i:j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res
    def isPal(self, cur, l, r):
            l , r = 0, len(cur) - 1
            while l < r:
                if cur[l] != cur[r]:
                    return False
                l += 1
                r -= 1 
            return True
