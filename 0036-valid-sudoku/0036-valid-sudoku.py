class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        
        m=len(board)
        n=len(board[0])
        for i in range(m):
            s=set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        
        for i in range(m):
            s=set()
            for j in range(n):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

        
        for i in range(0,m,3):
            for j in range(0,n,3):
                s=set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] != '.':
                            if board[k][l] in s:
                                return False
                            s.add(board[k][l])
        
        return True
        



        
        



        