class Solution:
    def reverse(self, x: int) -> int:
        s=''
        if x<0:
            a=abs(x)
            while a:
                s+=str(a%10)
                a=a//10
            final= (-1*int(s))
        elif x>0:
            a=x
            while a:
                s+=str(a%10)
                a=a//10
            final= (int(s))
        else:
            final= 0
        
        if -2**31<final<2**31-1:
            return final
        else:
            return 0
        