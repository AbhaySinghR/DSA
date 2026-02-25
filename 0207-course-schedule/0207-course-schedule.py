class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        inorder=[0]*numCourses

        for i,j in prerequisites:
            inorder[i]+=1
            graph[j].append(i)

        q=deque()
        topo=[]
        for i in range(len(inorder)):
            if inorder[i]==0:
                q.append(i)
        
        
        while q:
            n=q.popleft()
            topo.append(n)
            for j in graph[n]:
                inorder[j]-=1
                if inorder[j]==0:
                    q.append(j)
        
        if len(topo)==numCourses:
            return True
        else:
            return False


        