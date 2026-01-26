class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        
        if len(nums)<=1:
            return 0
        
        i=len(nums)-2
        while i>=0 and nums[i+1]>nums[i]:
            i-=1
        
        return i+1
