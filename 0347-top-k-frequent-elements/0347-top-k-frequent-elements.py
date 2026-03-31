class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hmap={}
        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        
        heap=[]
        li=[]
        for i,j in hmap.items():
                heapq.heappush(heap,(j,i))

                if len(heap)>k:
                    heapq.heappop(heap)
        
        for i,j in heap:
            li.append(j)
        return li