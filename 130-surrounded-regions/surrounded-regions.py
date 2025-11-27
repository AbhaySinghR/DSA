class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n=len(board)
        m=len(board[0])
        self.hmap={}

        def dfs(i,j,board):
            self.hmap[(i,j)]=1
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            for r,c in dir:
                n_i = i + r
                n_j = j + c
                if ((0<=n_i<len(board)) and (0<=n_j<len(board[0]))):
                    if board[n_i][n_j]=='O' and self.hmap[(n_i,n_j)]!=1:
                        dfs(n_i,n_j,board)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    self.hmap[(i,j)]=0

        for (i,j),val in self.hmap.items():
            if ((i==0 or i==n-1) or (j==0 or j==m-1)) and self.hmap[(i,j)]!=1:
                dfs(i,j,board)

        for (i,j), val in self.hmap.items():
            if val==0:
                board[i][j]='X'
