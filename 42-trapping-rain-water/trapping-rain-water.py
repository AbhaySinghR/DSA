class Solution:
    def trap(self, height: List[int]) -> int:

        st=[]
        water=0
        for i in range(len(height)):
            while st and height[i]>height[st[-1]]:
                idx=st.pop()
                if st:
                    h=min(height[st[-1]],height[i])-height[idx]
                    w=i-st[-1]-1
                    water+=h*w
            st.append(i)
        return water


        