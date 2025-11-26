class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        adjli={i: [] for i in range(len(isConnected))}

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and i!=j:
                    adjli[i].append(j)

        visited=set()
        cnt=0
        
        def dfs(i,adjli, visited):
            visited.add(i)
            for j in adjli.get(i,[]):
                if j not in visited:
                    dfs(j,adjli,visited)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i,adjli,visited)
                cnt+=1
        return cnt

        
        

        



        