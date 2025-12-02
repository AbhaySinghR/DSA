class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        visited=set()
        min_dis=float('inf')
        q=deque()
        n=len(maze)
        m=len(maze[0])
        q.append((entrance[0],entrance[1],0))
        visited.add((entrance[0],entrance[1]))
        
        while q:
            curr_i, curr_j, dis = q.popleft()
            
            if (((curr_i, curr_j) != (entrance[0], entrance[1])) and ((curr_i==0 or curr_i==n-1) or (curr_j==0 or curr_j==m-1))):
                return dis
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            for r,c in dir:
                n_i = curr_i + r
                n_j = curr_j + c
                if ((0<=n_i<n) and (0<=n_j<m)):
                    if (n_i,n_j) not in visited and maze[n_i][n_j]!="+":
                        q.append((n_i,n_j,dis+1))
                        visited.add((n_i,n_j))
        
        return -1
            
        