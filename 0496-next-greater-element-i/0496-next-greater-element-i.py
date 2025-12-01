class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        st=[]
        ans=[-1]*len(nums1)
        hmap={}
        for i in nums2:
            while st and st[-1]<i:
                hmap[st.pop()]=i
            st.append(i)
        for i in range(len(nums1)):
            if nums1[i] in hmap:
                ans[i]=hmap[nums1[i]]
            else:
                ans[i]=-1
        return ans
        