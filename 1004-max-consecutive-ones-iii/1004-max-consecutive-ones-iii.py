class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        max_len=0
        l,r=0,0
        cnt=0
        while r<len(nums):
            if nums[r]==0:
                cnt+=1
            
            while cnt>k and l<=r:
                if nums[l]==0:
                    cnt-=1
                l+=1

            max_len=max(max_len,r-l+1)
            r+=1
        
        return max_len


        