class Solution:
    def reverse(self, x: int) -> int:
        s=''
        if x<0:
            a=abs(x)
            while a:
                s+=str(a%10)
                a=a//10
            return (-1*int(s))
        elif x>0:
            a=x
            while a:
                s+=str(a%10)
                a=a//10
            return (int(s))
        else:
            return 0