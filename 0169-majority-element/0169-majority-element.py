class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hmap={}
        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        max_freq=float('-inf')
        res=0
        for i,j in hmap.items():
            if j>max_freq:
                max_freq=j
                res=i
        return res
                


        