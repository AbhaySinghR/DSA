class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indeg=[0]*numCourses
        adj_mat=defaultdict(list)

        for i, j in prerequisites:
            indeg[i]+=1
            adj_mat[j].append(i)
        
        q=deque()
        for i in range(len(indeg)):
            if indeg[i]==0:
                q.append(i)
        
        topo=[]
        while q:
            id=q.popleft()
            topo.append(id)
            for j in adj_mat[id]:
                indeg[j]-=1
                if indeg[j]==0:
                    q.append(j)
        
        if len(topo)==numCourses:
            return topo
        else:
            return []






        