class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        r=0
        sub_arr_sum=0
        min_len=float('inf')

        while r<len(nums):
            sub_arr_sum+=nums[r]
            while sub_arr_sum>=target:
                min_len=min(min_len,r-l+1)
                sub_arr_sum-=nums[l]
                l+=1
            r+=1

        if min_len==float('inf'):
            return 0
        return min_len

        