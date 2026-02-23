class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:



        m=len(image)
        n=len(image[0])
        vis=set()

        q=deque()
        start_pixel=image[sr][sc]
        q.append((sr,sc))
        while q:
            r,c=q.popleft()
            vis.add((r,c))
            image[r][c]=color
            dir=[(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in dir:
                n_i, n_j = dr + r, dc + c 
                if (n_i>=0 and n_i<m) and (n_j>=0 and n_j<n):
                    if image[n_i][n_j]==start_pixel and (n_i,n_j) not in vis:
                        image[n_i][n_j]=color 
                        vis.add((n_i,n_j))
                        q.append((n_i,n_j))
        
        return image
        