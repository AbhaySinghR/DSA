class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:


        m=len(grid)
        n=len(grid[0])
        vis=set()
        val=0

        def closed(i,j,vis,grid):
            isClosed=True
            q=deque()
            vis.add((i,j))
            q.append((i,j))
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            while q:
                r,c =q.popleft()
                if (r==0 or r==m-1) or (c==0 or c==n-1):
                    isClosed=False
                for dr,dc in dir:
                    n_i,n_j=r+dr,c+dc
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                            if grid[n_i][n_j]==0 and (n_i,n_j) not in vis:
                                q.append((n_i,n_j))
                                vis.add((n_i,n_j))
            
            if isClosed==True:
                return 1
            else:
                return 0

            



        for i in range(m):
            for j in range(n):
                if (i!=0 and i!=m-1) and (j!=0 and j!=n-1):
                    if grid[i][j]==0 and (i,j) not in vis:
                        val+=closed(i,j,vis,grid)
                        #print (val,i,j)
        
        return val