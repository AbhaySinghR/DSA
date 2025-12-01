class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:


        n=len(mat)
        m=len(mat[0])
        q=deque()
        visited=set()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        while q:
            curr_i,curr_j, dis= q.popleft()
            dir=[(0,1),(1,0),(0,-1),(-1,0)]
            for i,j in dir:
                new_i = i + curr_i
                new_j = j + curr_j
                if ((0<=new_i<n) and (0<=new_j<m)):
                    if (new_i,new_j) not in visited:
                        mat[new_i][new_j]=dis+1
                        q.append((new_i,new_j,dis+1))
                        visited.add((new_i,new_j))
        
        return mat
        
