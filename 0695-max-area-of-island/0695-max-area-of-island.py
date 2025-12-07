class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        n=len(grid)
        m=len(grid[0])
        visited=set()
        self.max_area=0


        def bfs(i,j,visited):
            q=deque()
            area=1
            q.append((i,j))
            while q:
                ci,cj=q.popleft()
                dir=[(0,1),(1,0),(0,-1),(-1,0)]
                for r,c in dir:
                    n_i = ci + r
                    n_j = cj + c
                    if ((0<=n_i<n) and (0<=n_j<m)) and (n_i,n_j) not in visited and grid[n_i][n_j]==1:
                        area+=1
                        visited.add((n_i,n_j))
                        q.append((n_i,n_j))

            self.max_area=max(self.max_area,area)  
            
            


        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j]==1:
                    visited.add((i,j))
                    bfs(i,j,visited)

        return self.max_area
        