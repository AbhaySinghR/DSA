class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:


        r,l=0,0
        cnt=0
        min_d=deque()
        max_d=deque()
        while r<len(nums):
            while min_d and nums[min_d[-1]]>nums[r]:
                min_d.pop()
            min_d.append(r)
            while max_d and nums[max_d[-1]]<nums[r]:
                max_d.pop()
            max_d.append(r)

            while  (nums[max_d[0]]- nums[min_d[0]])* (r-l+1)>k:
                if min_d[0]==l:
                    min_d.popleft()
                if max_d[0]==l:
                    max_d.popleft()
                l+=1
            
            cnt+=(r-l+1)
            r+=1
        
        return cnt
            
        

            

            
        

            