class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n=len(nums)
        st=[]
        res=[-1]*len(nums)
        for i in range(n*2):
            while st and nums[i%n]>nums[st[-1]]:
                a=st.pop()
                res[a]=nums[i%n]
            if i < n:
                st.append(i)
            
        
        return res



        