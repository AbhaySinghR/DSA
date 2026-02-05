class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def cntf (goal,nums):
            if goal<0:
                return 0
            l,r=0,0
            s=0
            cnt=0
            while r<len(nums):
                s+=nums[r]
                while s>goal:
                    s-=nums[l]
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
    
        return cntf(goal,nums)-cntf(goal-1,nums)
            
        
        