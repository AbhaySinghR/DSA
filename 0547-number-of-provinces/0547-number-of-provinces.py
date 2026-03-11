class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:


        n=len(isConnected)
        vis=set()
        cnt=0
        q=deque()
        for i in range(n):
            if i not in vis:
                cnt+=1
                q.append(i)
            
            while q:
                c=q.popleft()
                for j in range(n):
                    if isConnected[c][j]==1 and j not in vis:
                        vis.add(j)
                        q.append(j)
            
        return cnt