class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        l,r=0,0
        cost=0
        max_len=float('-inf')
        while r<len(s):

            cost+=abs(ord(s[r])-ord(t[r]))
            while cost>maxCost:
                temp=abs(ord(s[l])-ord(t[l]))
                cost-=temp
                l+=1
            
            max_len=max(max_len,r-l+1)
            r+=1
        
        return max_len


        