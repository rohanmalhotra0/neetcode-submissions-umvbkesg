class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        i = 0
        while i < len(edge):
            if edge[i][1] == edge[i+1][1]:
                return edge[i]
            i +=1
                