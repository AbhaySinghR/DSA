class Solution:
    def minFlips(self, s: str) -> int:

        n=len(s)
        s=s+s
        l=0
        r=n
        diff1,diff2=0,0
        p1=''
        p2=''
        min_cnt=0
        for i in range(len(s)):
            if i%2==0:
                p1+='0'
                p2+='1'
            else:
                p1+='1'
                p2+='0'
        for i in range(l, r):
            if s[i] != p1[i]:
                diff1 += 1
            if s[i] != p2[i]:
                diff2 += 1
        min_cnt=min(diff1,diff2)
        while r<len(s):

            if s[l]!=p1[l]:
                diff1-=1
            if s[l]!=p2[l]:
                diff2-=1

            if s[r]!=p1[r]:
                diff1+=1
            if s[r]!=p2[r]:
                diff2+=1
            
            min_cnt=min(min_cnt,diff1,diff2)
            r+=1
            l+=1
        
        return min_cnt
            

        


