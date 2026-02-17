class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final_res=set()
        for i in range(len(nums)):
            s=set()
            for j in range(i+1,len(nums)):
                if 0 - (nums[i]+nums[j]) in s:
                    triplet = tuple(sorted([nums[i], nums[j],  0 - (nums[i]+nums[j])]))
                    final_res.add(triplet)
                s.add(nums[j])
        
        li=list(final_res)
        return li





        