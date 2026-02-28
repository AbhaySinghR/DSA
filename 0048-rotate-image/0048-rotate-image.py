class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        m=len(matrix)
        n=len(matrix[0])
        vis=set()
        for i in range(m):
            for j in range(n):
                if i==j:
                    continue
                elif (i,j) not in vis and (j,i) not in vis:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                    vis.add((i,j))
                    vis.add((j,i))     
        
        k=0
        while k<m:
            i=0
            j=n-1
            while i<j:
                matrix[k][i],matrix[k][j]=matrix[k][j],matrix[k][i]
                i+=1
                j-=1
            k+=1
        
        