class Solution:
    def maxVowels(self, s: str, k: int) -> int:


        vli=['a','e','i','o','u']
        
        max_v=float('-inf')
        cnt=0
        for i in range(k):
            if s[i] in vli:
                cnt+=1
        
        max_v=max(max_v,cnt)
        r=k
        l=0
        while r<len(s):

            if s[r] in vli:
                cnt+=1
            
            if r-l+1>k:
                if s[l] in vli:
                    cnt-=1
                l+=1
            
            if r-l+1==k:
                max_v=max(max_v,cnt)
            
            r+=1
        return max_v

        

        