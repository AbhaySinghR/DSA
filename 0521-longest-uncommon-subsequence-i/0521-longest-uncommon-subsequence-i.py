class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        i,j=0,0

        if len(a)<len(b):
            return len(b)
        elif len(a)>len(b):
            return len(a)
        else:
            while i<len(a) and j<len(b):
                if a[i]==b[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
        
        if j==len(b) and i!=len(a):
            return j
        return -1
        


        