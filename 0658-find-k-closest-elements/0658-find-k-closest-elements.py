class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap=[]
        for i in range(len(arr)):
            dist=abs(arr[i]-x)
            heapq.heappush(heap,(-dist, -arr[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        
        li=[]
        while heap:
            dist,ele=heapq.heappop(heap)
            ele=ele*-1
            li.append(ele)
        
        return sorted(li)
            
        

        