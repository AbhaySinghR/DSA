class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        hmap={0:1}
        cnt=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        print (nums)
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            diff = s-k
            if diff in hmap:
                cnt=cnt+hmap[diff]
            hmap[s]=hmap.get(s,0)+1
        
        return cnt


        