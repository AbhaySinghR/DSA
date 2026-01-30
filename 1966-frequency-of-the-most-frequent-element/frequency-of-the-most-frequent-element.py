class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums=sorted(nums)
        l,r=0,0
        tot,max_ele=0,0
        while r<len(nums):
            tot+=nums[r]
            while nums[r]*(r-l+1)>tot+k:
                tot-=nums[l]
                l+=1
            
            max_ele=max(max_ele,r-l+1)
            r+=1
        return max_ele
            