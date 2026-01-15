class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li=[]
        plr=[1]*len(nums)
        prl=[1]*len(nums)
        for i in range(len(nums)):
            if i!=0:
                plr[i]=nums[i-1]*plr[i-1]

        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                prl[i]=nums[i+1]*prl[i+1]
        
        for i in range(len(nums)):
            li.append(plr[i]*prl[i])
        
        return li


        