class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pref =[]
        prd=1
        for i in range(len(nums)):
            pref.append(prd)
            prd=prd*nums[i]

        suff=[1]*len(nums)
        pred=1
        for i in range(len(nums)-1,-1,-1):
            suff[i]=pred
            pred*=nums[i]
        
        li=[1]*len(nums)
        for i in range(len(nums)):
            li[i]=pref[i]*suff[i]
        return li

        