class Solution:
    def fib(self, n: int) -> int:

        if n==0:
            return 0
        if n==1:
            return 1
        
        first=0
        second=1
        f_sum=0
        for i in range(1,n):
            f_sum=first+second
            first,second=second,f_sum
        
        return f_sum

        