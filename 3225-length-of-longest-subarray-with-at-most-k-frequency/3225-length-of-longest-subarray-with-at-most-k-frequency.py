class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        left=0
        right=0
        max_len=0
        hmap={}
        for right in range(len(nums)):
            hmap[nums[right]]=hmap.get(nums[right],0)+1
            while hmap[nums[right]]>k:
                hmap[nums[left]]-=1
                left+=1
            
            max_len=max(max_len,right-left+1)
        
        return max_len
        