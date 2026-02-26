class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        m=len(grid)
        n=len(grid[0])
        t=0
        q=deque()
        vis=set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,t))
        
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r,c,t=q.popleft()
            vis.add((r,c))
            for dr, dc in dir:
                n_i,n_j=r+dr, c+dc
                if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                    if grid[n_i][n_j]==1 and (n_i,n_j) not in vis:
                        q.append((n_i,n_j,t+1))
                        vis.add((n_i,n_j))
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    return -1
        
        return t



        