class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        hmap={}
        min_element=float('inf')
        for i in range(len(nums)):
            if nums[i]%2==0:
                hmap[nums[i]]=hmap.get(nums[i],0)+1
        if len(hmap):
            idx=max(hmap,key=hmap.get)
            max_freq=hmap[idx]
            for i,j in hmap.items():
                if j==max_freq:
                    min_element=min(min_element,i)
        else:
            return -1
        
        print (hmap)
        return min_element



        