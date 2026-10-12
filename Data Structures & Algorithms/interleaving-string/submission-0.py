class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s4 = s1+s2
        countS = Counter(s4)
        count3 = Counter(s3)

        return countS == count3
        
        
        """if not s1 and s2 and s3: return True
        def dfs(i , j, currStr):
            if i >= len(s1):
                return False
            if j >= len(s2)
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            if currStr == s3:
                return True
            memo[(i,j)] = dfs(i+1, j, currStr + s1[i]) or dfs(i, j + 1 , currStr + s2[j]) 
                
            
            memo[(i, j)]"""