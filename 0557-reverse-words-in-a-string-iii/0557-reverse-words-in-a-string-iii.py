class Solution:
    def reverseWords(self, s: str) -> str:

        li=s.split(' ')

        for i in range(len(li)):
            a=li[i]
            li[i]=a[::-1]

        res=''
        for i in range(len(li)):
            if i!=len(li)-1:
                res+=li[i]+' '
            else:
                res+=li[i]

        return res
                
        