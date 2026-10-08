class Solution:
    def isPathCrossing(self, path: str) -> bool:
       
        m = {"N" : 1, "S" : -1, "W" : 1, "E" : -1}
        curr = (0, 0)
        visit = set()
        visit.add(curr)
        
        for c in path:
            if c in 'NS':
                a = curr[1] + m[c]
                temp = (curr[0], a)
                curr = temp
            else:
                b = curr[0] + m[c]
                temp = (b, curr[1])
                curr = temp
            
            if curr in visit:
                return False
            visit.add(curr)
        return True
            

            
        