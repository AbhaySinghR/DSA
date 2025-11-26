class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        cnt=0
        visited = [[0 for _ in range(m)] for _ in range(n)]

        def bfs(i,j,visited,grid):
            visited[i][j]=1
            q=deque()
            q.append((i, j))
            while q:
                i_d,j_d=q.popleft()
                dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in dirs:
                    n_i = i_d + dr
                    n_j = j_d + dc
                    if 0 <= n_i < n and 0 <= n_j < m:
                        if grid[n_i][n_j] == "1" and visited[n_i][n_j] == 0:
                            visited[n_i][n_j] = 1
                            q.append((n_i, n_j))

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j]==0:
                    cnt+=1
                    bfs(i,j,visited,grid)
        
        return cnt

