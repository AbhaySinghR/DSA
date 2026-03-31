class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hmap={}
        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        
        heap=[]

        for i,j in hmap.items():
            heapq.heappush(heap,(-j,i))
        
        print (heap)
        li=[]
        while k>0:
            f,ky=heapq.heappop(heap)
            li.append(ky)
            k-=1
        
        return li