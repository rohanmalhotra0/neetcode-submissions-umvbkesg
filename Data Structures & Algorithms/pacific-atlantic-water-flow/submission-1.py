class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        atlantic = set()
        pacific = set()

        rows, cols = len(heights), len(heights[0])

        pacificQ = deque()
        atlanticQ = deque()

        for i in range (rows):
            pacificQ.append((i,0))
            pacific.add((i,0))  
        for i in range (cols):
            pacificQ.append((0,i))
            pacific.add((0,i))
        for i in range (rows):
            atlanticQ.append((len(i)-1,0))
            atlantic.add((len(i)-1,0))  
        for i in range (cols):
            atlanticQ.append((0,len(i)-1))
            atlantic.add((0,len(i)-1))     
        
        def bfs(q,visited):
            x,y = q.popleft()
            for dx, dy in directions:
                nx,ny = dx+x, dy+y
                if(
                    0<=nx<rows and 
                    0<=ny<cols and 
                    heights[nx][ny] not in visited and
                    heights[nx][ny] >= heights[x][y]
                ):
                    q.append((nx,ny))
                    visited.add((nx,ny))

        bfs(atlanticQ,atlantic)
        bfs(pacificQ,pacific)


        return list(atlantic.intersetion(pacific))
