class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        i,j=0,0
        
        if len(t)<len(s):
            return False
       
        while j<len(t) and i<len(s):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1

        if i==len(s) or len(s)==0:
            return True
        return False
