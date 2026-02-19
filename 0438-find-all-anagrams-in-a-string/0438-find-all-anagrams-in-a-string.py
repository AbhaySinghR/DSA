class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        idx=[]
        hmap1={}
        n=len(p)
        for i in range(len(p)):
            hmap1[p[i]]=hmap1.get(p[i],0)+1
        

        i,j=0,0
        hmap2={}
        while j<len(s):

            hmap2[s[j]]=hmap2.get(s[j],0)+1

            if j-i+1>n:
                if hmap2[s[i]]>1:
                    hmap2[s[i]]-=1
                else:
                    del hmap2[s[i]]
                i+=1
            
            if j-i+1==n:
                if hmap1==hmap2:
                    idx.append(i)
            
            j+=1
        
        return idx

        