class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hmap={}
        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        
        a=sorted(hmap.items(),key=lambda X:X[1],reverse=True)
        cnt=1
        li=[]
        for i,j in a:
            if cnt<=k:
                li.append(i)
                cnt+=1
            else:
                break 
        

        return li
