class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water=float('-inf')
        i,min_h=0,0
        j=len(height)-1
        while i<j:
            min_h=min(height[i],height[j])
            width=j-i
            max_water=max(max_water,min_h*width)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return max_water
        