class Solution:
    def reverseWords(self, s: str) -> str:

        li=s.split(' ')
        res=''
        print (li)
        f_li=[]
        for i in li:
            if i!='':
                f_li.append(i)

        for i in range(len(f_li)-1,-1,-1):
            if i!=0:
                res+=f_li[i]+" "
            else:
                res+=f_li[i]
        
        return res

        