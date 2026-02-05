class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l,r=0,0
        cnt=0
        p=1
        if k<=1:
            return 0
        while r<len(nums):
            if nums[r]==0:
                l=r+1
                p=1
                continue
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            cnt+=(r-l+1)
            r+=1
        
        return cnt
        