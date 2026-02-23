class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        m=len(grid)
        n=len(grid[0])
        vis_arr=[]
        cnt=0
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(0)
            vis_arr.append(row)
        
        def nIsl(i,j,grid,vis_arr):
            vis_arr[i][j]=1
            q=deque()
            q.append((i,j))
            while q:
                r,c= q.popleft()
                dir=[(0,1),(1,0),(0,-1),(-1,0)]
                for dr, dc in dir:
                    n_r,n_c=r+dr,c+dc
                    if (n_r>=0 and n_r<m) and (n_c>=0 and n_c <n):
                        if grid[n_r][n_c]=="1" and vis_arr[n_r][n_c]!=1:
                            vis_arr[n_r][n_c]=1  
                            q.append((n_r,n_c))     

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and vis_arr[i][j]!=1:
                    cnt+=1
                    nIsl(i,j,grid,vis_arr)
        
        return cnt

        