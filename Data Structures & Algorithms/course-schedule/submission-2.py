class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m  = defaultdict(list)
        for crs, pre in prerequisites:
            m[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if m[crs] == []:
                return True
            visit.add(crs)
            for pre in m[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            m[crs] = []
            return True
        
        return dfs(0)