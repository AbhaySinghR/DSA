class Solution:
    def reverseWords(self, s: str) -> str:

        li=s.split()
        res=''
        for i in range(len(li)-1,-1,-1):
            if i!=0:
                res+=li[i]+" "
            else:
                res+=li[i]
        
        return res

        