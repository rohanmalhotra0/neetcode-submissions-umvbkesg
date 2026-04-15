class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        i = 1
        while i < len(edges):
            if edges[i][1] == edges[i-1][1]:
                return edges[i]
            i +=1
                