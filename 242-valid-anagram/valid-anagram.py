class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap1={}
        hmap2={}
        for i in range(len(s)):
            hmap1[s[i]]=hmap1.get(s[i],0)+1

        for i in range(len(t)):
            hmap2[t[i]]=hmap2.get(t[i],0)+1
        
        if hmap1==hmap2:
            return True
        return False
