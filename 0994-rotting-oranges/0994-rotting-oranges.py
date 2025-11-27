class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n=len(grid)
        m=len(grid[0])
        minute=0
        q=deque()
        visited=set()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            size=len(q)
            while size:
                i,j,t = q.popleft()
                for r,c in dir:
                    n_i = i + r
                    n_j = j + c
                    if ((n_i>=0 and n_i<n) and (n_j>=0 and n_j<m)):
                        if grid[n_i][n_j]==1 and (n_i,n_j) not in visited:
                            grid[n_i][n_j]=2
                            q.append((n_i,n_j,t+1))
                            visited.add((n_i,n_j,t+1))
                size-=1
            minute=t
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return minute