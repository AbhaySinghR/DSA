class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hmap={0:1}
        s,cnt=0,0
        for i in range(len(nums)):
            s+=nums[i]
            diff=s-k
            if diff in hmap:
                cnt=cnt+hmap[diff]
            hmap[s]=hmap.get(s,0)+1
        
        return cnt



        
        