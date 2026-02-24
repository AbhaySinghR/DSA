class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:


        m=len(maze)
        n=len(maze[0])
        vis=set()
        q=deque()
        q.append((entrance[0],entrance[1],0))
        vis.add((entrance[0],entrance[1]))
        

        def fun(q,vis,grid):
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            while q:
                r,c,dis=q.popleft()
                for dr, dc in dir:
                    n_i,n_j=r+dr,c+dc
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if maze[n_i][n_j]=="." and (n_i,n_j) not in vis:
                            if (n_i==0 or n_i==m-1) or (n_j==0 or n_j==n-1):
                                return dis+1
                            q.append((n_i,n_j,dis+1))
                            vis.add((n_i,n_j))
            return -1

        return fun(q,vis,maze)

        
        
