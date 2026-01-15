class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        l=0
        r=len(nums)-1
        start,end=-1,-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                if m==0 or nums[m-1]!=target:
                    start=m
                r=m-1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1

        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                if m==len(nums)-1 or nums[m+1]!=target:
                    end=m
                l=m+1
            if nums[m]>target:
                r=m-1
            else:
                l=m+1
        
        return [start,end]