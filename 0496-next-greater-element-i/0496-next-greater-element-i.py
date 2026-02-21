class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res=[-1]*len(nums2)
        st=[]   
        for i in range(len(nums2)):
            while st and nums2[i] > nums2[st[-1]]:
                a=st.pop()
                res[a]=nums2[i]
            st.append(i)
        
        hmap={}
        for i in range(len(nums2)):
            hmap[nums2[i]]=res[i]

        final_res=[]
        for i in range(len(nums1)):
            final_res.append(hmap[nums1[i]])

        return final_res        