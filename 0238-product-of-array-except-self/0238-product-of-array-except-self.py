class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref=[1]*len(nums)
        suff=[1]*len(nums)
        output=[1]*len(nums)

        prod=1
        for i in range(len(nums)):
            pref[i]=prod
            prod*=nums[i]
        prod=1
        for i in range(len(nums)-1,-1,-1):
            suff[i]=prod
            prod*=nums[i]
        
        for i in range(len(nums)):
            output[i]=pref[i]*suff[i]
        
        return output
        