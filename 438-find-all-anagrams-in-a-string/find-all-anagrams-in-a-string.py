class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        if len(p)>len(s):
            return []
        idx=[]
        pmap={}
        smap={}
        for i in range(len(p)):
            pmap[p[i]]=pmap.get(p[i],0)+1
            smap[s[i]]=smap.get(s[i],0)+1
        
        if pmap==smap:
            idx.append(0)
        l=0
        r=len(p)
        while r<len(s):
            smap[s[r]]=smap.get(s[r],0)+1
            smap[s[l]]=smap.get(s[l],0)-1
            if smap[s[l]]==0:
                del smap[s[l]]
            if smap==pmap:
                idx.append(l+1)
            l+=1
            r+=1
        
        return idx
            



        





        