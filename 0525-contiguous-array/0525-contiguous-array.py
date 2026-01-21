class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s=0  
        long_len=0
        hmap={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                s+=1
            else:
                s+=-1
            if s in hmap:
                long_len=max(long_len,i-hmap[s])
            else:
                hmap[s]=i
        

        return long_len

