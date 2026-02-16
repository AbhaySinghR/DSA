class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n=len(nums)
        temp_li=nums[n-k:]
        j=n-1
        i=n-k-1
        while i>=0:
            nums[j]=nums[i]
            j-=1
            i-=1
        
        while j>=0:
            nums[j]=temp_li[j]
            j-=1
        
