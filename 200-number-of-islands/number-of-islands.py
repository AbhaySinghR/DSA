class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m=len(grid)
        n=len(grid[0])
        vis=set()

        def nIsl(i,j,vis,grid):
            q=deque()
            q.append((i,j))
            cnt=0
            vis.add((i,j))
            dir =[(0,1),(1,0),(0,-1),(-1,0)]
            while q:
                r,c =q.popleft()
                for dr, dc in dir:
                    n_i,n_j = r+dr,c+dc
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if grid[n_i][n_j]=="1" and (n_i,n_j) not in vis:
                            q.append((n_i,n_j))
                            vis.add((n_i,n_j))
            
            return cnt+1 

        res=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in vis:
                    res+=nIsl(i,j,vis,grid)
        return res