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
        
        for i in range (cols):
            atlanticQ.append((rows-1,i))
            atlantic.add((rows-1,i))  
        for i in range (rows):
            atlanticQ.append((i,cols-1))
            atlantic.add((i,cols-1))     
        
        def bfs(q,visited):
            x,y = q.popleft()
        
            for dx, dy in directions:
                nx,ny = dx+x, dy+y
                if(
                    0<=nx<rows and 
                    0<=ny<cols and 
                    (nx, ny) not in visited and
                    heights[nx][ny] >= heights[x][y]
                ):
                    q.append((nx,ny))
                    visited.add((nx,ny))


        bfs(atlanticQ,atlantic)
        bfs(pacificQ,pacific)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
        return res

       # return list(atlantic.intersection(pacific))
