class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:


        hmap={}
        l,r=0,0
        max_score=float('-inf')
        score=0
        while r<len(nums):

            score+=nums[r]

            if nums[r] in hmap:
                pos=hmap[nums[r]]
                while l<=pos:
                    score-=nums[l]
                    l+=1

            hmap[nums[r]]=r
            max_score=max(max_score,score)
            r+=1
        return max_score

            





        