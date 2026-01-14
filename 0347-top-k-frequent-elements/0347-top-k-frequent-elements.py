class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li=[]
        hmap={}
        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        
        items = list(hmap.items())
        items.sort(key=lambda x: x[1],reverse=True)
        
        for i in range(k):
            li.append(items[i][0])
        
        return li





        