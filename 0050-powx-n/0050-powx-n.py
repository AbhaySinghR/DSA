class Solution:
    def myPow(self, x: float, n: int) -> float:

        p=abs(n)
        f=1
        while p:
            if p%2==1:
                f=f*x
            x*=x
            p=p//2
        
        if n<0:
            return 1/f
        return f
        