class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        m=len(grid)
        n=len(grid[0])
        q=deque()
        vis=set()
        mins=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis.add((i,j))

        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            size=len(q)
            while size:
                i,j,t=q.popleft()
                for dr, dc in dir:
                    n_i,n_j=dr+i,dc+j
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if grid[n_i][n_j]==1 and (n_i,n_j) not in vis:
                            grid[n_i][n_j]=2
                            vis.add((n_i,n_j))
                            q.append((n_i,n_j,t+1))
                size-=1
            mins=t
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        
        return mins



        