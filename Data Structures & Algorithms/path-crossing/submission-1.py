class Solution:
    def isPathCrossing(self, path: str) -> bool:
       
        m = {"N" : 1, "S" : -1, "W" : 1, "E" : -1}
        start = curr = [0, 0]
        
        for c in path:
            if c in 'NS':
                curr[1] += m[dy]
            else:
                curr[0] += m[dx]
            if curr == start:
                return False
        return True
            

            
        