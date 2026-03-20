class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n=len(mat)
        m=len(mat[0])
        li=[0]*(m*n)
        k=0

        diag=(m+n)-1

        for i in range(diag):
            if i%2==0:
                for x in range(min(i, n - 1), -1, -1):
                    y=i-x
                    if 0 <= x < n and 0 <= y < m:
                        li[k]=mat[x][y]
                        k+=1
            else:
                for x in range(0, min(i, n - 1) + 1):
                    y = i - x
                    if 0 <= x < n and 0 <= y < m:
                        li[k] = mat[x][y]
                        k += 1
        
        return li


        