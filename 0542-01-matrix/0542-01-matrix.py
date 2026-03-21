class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m=len(mat)
        n=len(mat[0])
        q=deque()
        vis=set()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    vis.add((i,j))


        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r,c,d=q.popleft()
            if mat[r][c]==1:
                mat[r][c]=d
            for dr,dc in dir:
                n_i,n_j=r+dr,c+dc
                if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                    if mat[n_i][n_j]==1 and (n_i,n_j) not in vis:
                        q.append((n_i,n_j,d+1))
                        vis.add((n_i,n_j))


        return mat
