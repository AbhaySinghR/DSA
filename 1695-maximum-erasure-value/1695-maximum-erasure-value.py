class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:


        l,r,=0,0
        max_sum=0
        final=float('-inf')
        hmap={}
        while r<len(nums):
            if nums[r] in hmap:
                idx=hmap[nums[r]]
                while l<=idx:
                    max_sum-=nums[l]
                    del hmap[nums[l]]
                    l+=1

            hmap[nums[r]]=r
            max_sum+=nums[r]
            final=max(final,max_sum)
            r+=1
        
        return final
        