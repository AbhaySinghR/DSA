class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        streak=1
        res=[]
        if len(nums)==1:
            return [nums[0]]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]+1:
                streak+=1
            else:
                streak=1
            
            if i>=k-1:
                if streak>=k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        
        return res




        