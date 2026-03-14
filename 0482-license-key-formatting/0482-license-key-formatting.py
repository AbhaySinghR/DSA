class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        st=''
        for i in s:
            if i!='-':
                st+=i.upper()
        li=[]
        for j in range(len(st)-1,-1,-k):
            li.append(st[max(0,j-k+1):j+1])
        final=''
        for j in range(len(li)-1,-1,-1):
            if j==0:
                final+=li[j]
            else:
                final+=li[j]+'-'
        return final
            
        
            
            


        
                
            
                

        
        