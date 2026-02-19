class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        

        sum_win=0
        l,r=0,0
        cnt=0
        while r<len(arr):

            sum_win+=arr[r]

            if r-l+1>k:
                sum_win-=arr[l]
                l+=1
            
            if r-l+1==k:
                if (sum_win//k)>=threshold:
                    cnt+=1
            
            r+=1
        
        return cnt