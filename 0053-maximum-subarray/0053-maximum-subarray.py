class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        min_pre,presum=0,0
        max_sum=float('-inf')
        for i in range(len(nums)):
            presum=presum+nums[i]
            max_sum=max(max_sum,presum-min_pre)
            min_pre=min(min_pre,presum)
        
        return max_sum



        