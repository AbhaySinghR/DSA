class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n=len(grid)
        m=len(grid[0])
        cnt=0
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        def dfs(i,j,visited,grid):
            visited[i][j]=1
            dir=[(-1,0),(1,0),(0,1),(0,-1)]
            for r,c in dir:
                n_i=i+r
                n_j=j+c
                if (n_i>=0 and n_i<len(grid)) and (n_j>=0 and n_j<len(grid[0])) and (grid[n_i][n_j]=="1") and (visited[n_i][n_j]!=1):
                    dfs(n_i,n_j,visited,grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j]!=1:
                    cnt+=1
                    dfs(i,j,visited,grid)
        
        return cnt
        