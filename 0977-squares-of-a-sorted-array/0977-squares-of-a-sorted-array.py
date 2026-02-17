class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        i=0
        k,j=len(nums)-1,len(nums)-1
        res=[0]*len(nums)
        while i<=j:
            l=nums[i]*nums[i]
            r=nums[j]*nums[j]
            if l<r:
                res[k]=r
                j-=1
                k-=1
            elif l>r:
                res[k]=l
                i+=1
                k-=1
            else:
                res[k]=l
                k-=1
                i+=1
        return res



        