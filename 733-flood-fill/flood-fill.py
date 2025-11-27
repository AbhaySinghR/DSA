class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

     
        init=image[sr][sc]
        if init == color:
            return image
        image[sr][sc]=color
        q=deque()
        q.append((sr,sc))
        while q:
            i,j=q.popleft()
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for r,c in dir:
                n_i=i+r
                n_j=j+c
                if ((n_i>=0 and n_i<len(image)) and (n_j>=0 and n_j<len(image[0]))):
                    if image[n_i][n_j]==init:
                        q.append((n_i,n_j))
                        image[n_i][n_j]=color
        
        return image
        