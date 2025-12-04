class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:


        n=len(grid)
        m=len(grid[0])
        visited=set()
        q=deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and ((i==0 or i==n-1) or (j==0 or j==m-1)):
                    q.append((i,j))
                    visited.add((i,j))
        
        while q:
            i,j = q.popleft()
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            for r,c in dir:
                n_i = i + r
                n_j = j + c
                if ((0<=n_i<n) and (0<=n_j<m)) and (n_i,n_j) not in visited:
                    if grid[n_i][n_j]==0:
                        q.append((n_i,n_j))
                        visited.add((n_i,n_j))
        
        cnt=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and (i,j) not in visited:
                    q=deque()
                    q.append((i,j))
                    visited.add((i,j))
                    while q:
                        curr_i,curr_j = q.popleft()
                        dir=[(0,1),(1,0),(0,-1),(-1,0)]
                        for r,c in dir:
                            n_i = curr_i + r
                            n_j = curr_j + c
                            if ((0<=n_i<n) and (0<=n_j<m)) and (n_i,n_j) not in visited:
                                if grid[n_i][n_j]==0:
                                    q.append((n_i,n_j))
                                    visited.add((n_i,n_j))
                    cnt+=1
            
        return cnt

