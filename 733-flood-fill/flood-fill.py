class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

     
        def dfs(i,j,image):
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for r,c in dir:
                n_i=i+r
                n_j=j+c
                if ((n_i>=0 and n_i<len(image)) and (n_j>=0 and n_j<len(image[0]))):
                    if image[n_i][n_j]==self.init:
                        image[n_i][n_j]=color
                        dfs(n_i,n_j,image)        
        self.init=image[sr][sc]
        if self.init == color:
            return image
        image[sr][sc]=color
        dfs(sr,sc,image)
        return image
        