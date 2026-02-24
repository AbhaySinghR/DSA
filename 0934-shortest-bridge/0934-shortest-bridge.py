class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:


        m=len(grid)
        n=len(grid[0])
        vis=set()

        def fisl(i,j,grid):
            q=deque()
            fis=deque()
            q.append((i,j))
            vis.add((i,j))
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            while q:
                r,c,=q.popleft()
                fis.append((r,c,0))
                for dr, dc in dir:
                    n_i,n_j = r+dr, c+dc
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if grid[n_i][n_j]==1 and (n_i,n_j) not in vis:
                            q.append((n_i,n_j))
                            vis.add((n_i,n_j))
            return fis

        def bridge(q,vis,grid):
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            while q:
                r,c,dis = q.popleft()
                for dr, dc in dir:
                    n_i,n_j = r+dr, c+dc
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if (n_i,n_j) not in vis:
                            if grid[n_i][n_j]==1:
                                return dis
                            q.append((n_i,n_j,dis+1))
                            vis.add((n_i,n_j))

        
        def ff(m,n):
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        return fisl(i,j,grid)

        fisland = ff(m,n)
        d=bridge(fisland,vis,grid)
        return d

        
        

        




        