class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s=set(nums)

        max_c=0
        for i in s:
            if i-1 not in s:
                cnt=1
                curr=i

                while curr+1 in s:
                    cnt+=1
                    curr+=1
            
                max_c=max(cnt,max_c)
        
        return max_c



        
