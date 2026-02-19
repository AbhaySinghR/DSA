class Solution:
    def minWindow(self, s: str, t: str) -> str:


        hmap={}
        for i in range(len(t)):
            hmap[t[i]]=hmap.get(t[i],0)+1
        
        req=len(hmap)

        l,r=0,0
        hmap2={}
        ans=""
        formed=0
        min_len=float('inf')
        while r<len(s):

            hmap2[s[r]]=hmap2.get(s[r],0)+1

            if s[r] in hmap and hmap2[s[r]]==hmap[s[r]]:
                formed+=1
            
            while formed==req:

                if r-l+1<min_len:
                    ans=s[l:r+1]
                    min_len=r-l+1
                
                hmap2[s[l]]-=1
                if s[l] in hmap and hmap2[s[l]]<hmap[s[l]]:
                    formed-=1
                l+=1
            
            r+=1
        
        return ans
                    


        