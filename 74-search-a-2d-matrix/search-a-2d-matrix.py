class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        k=0
        m=len(matrix)
        n=len(matrix[0])

        if m==n==1:
            if matrix[0][0]==target:
                return True
            else:
                return False

        while k<m:
            l=0
            r=n-1
            while l<=r:
                mid=(l+r)//2
                if matrix[k][mid]==target:
                    return True
                elif matrix[k][mid]>target:
                    r-=1
                else:
                    l+=1

            k+=1

        return False        