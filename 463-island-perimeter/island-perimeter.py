class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=set()
        q=deque()
        per=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==1 and (i,j) not in visited:
                    visited.add((i,j))
                    q.append((i,j))
                    break



        while q:
            i,j=q.popleft()
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            for r,c in dir:
                n_i = i + r 
                n_j = j + c 
                if not ((0<=n_i<n) and (0<=n_j<m)):
                    per+=1
                elif grid[n_i][n_j]==0:
                    per+=1
                elif (n_i, n_j) not in visited:
                    visited.add((n_i, n_j))
                    q.append((n_i, n_j))

        return per    