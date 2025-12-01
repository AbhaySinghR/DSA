class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        ans=[-1]*n
        for i in range(2*n):
            while st and nums[st[-1]]<nums[i%n]:
                id=st.pop()
                ans[id]=nums[i%n]
            if i < n:
                st.append(i)
        return ans
        