class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i,isConnected,visited):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and j not in visited:
                    dfs(j,isConnected,visited)
        
        visited=set()
        cnt=0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i,isConnected,visited)
                cnt+=1
        return cnt

       
        
        

        



        