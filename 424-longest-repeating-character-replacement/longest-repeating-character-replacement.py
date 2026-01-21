class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        long_sub=0
        start=0
        hmap={}
        max_freq=0
        for i in range(len(s)):
            hmap[s[i]]=hmap.get(s[i],0)+1
            max_freq=max(max_freq,hmap[s[i]])
            while (i - start + 1)-max_freq>k:
                hmap[s[start]]=hmap.get(s[start])-1
                start+=1
            
            long_sub=max(i-start+1,long_sub)
        
        return long_sub






        