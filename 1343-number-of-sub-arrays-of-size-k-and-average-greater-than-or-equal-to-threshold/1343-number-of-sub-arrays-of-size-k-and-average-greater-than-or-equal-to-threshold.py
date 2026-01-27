class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        cnt=0
        win_sum=0

        # Getting first window
        for i in range(k):
            win_sum+=arr[i]
        
        if win_sum/k>=threshold:
            cnt+=1
        
        l=0
        r=k
        while r<len(arr):
            win_sum+=arr[r]
            win_sum-=arr[l]

            if win_sum/k>=threshold:
                cnt+=1
            
            l+=1
            r+=1
        
        return cnt

        


        
        


        