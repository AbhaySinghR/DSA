class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m=len(board)
        n=len(board[0])
        vis=set()


        def Surr(i,j,board,vis):
            vis.add((i,j))
            q=deque()
            q.append((i,j))
            while q:
                r,c=q.popleft()
                dir=[(0,1),(1,0),(-1,0),(0,-1)]
                for dr, dc in dir:
                    n_i,n_j=dr+r, dc+c
                    if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                        if board[n_i][n_j]=="O" and (n_i,n_j) not in vis:
                            vis.add((n_i,n_j))
                            q.append((n_i,n_j))

        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in vis:
                    if (i==0 or i==m-1) or (j==0 or j==n-1):
                        Surr(i,j,board,vis)
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and board[i][j]=="O":
                    board[i][j]="X"





        