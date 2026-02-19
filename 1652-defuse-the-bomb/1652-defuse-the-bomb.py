class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n=len(code)
        res=[0]*len(code)
        sum_win=0
        if k==0:
            return res
        elif k>0:
            for i in range(len(code)):
                t=0
                while t<k:
                    idx=(i+1+t)%n
                    sum_win+=code[idx]
                    t+=1
                res[i]=sum_win
                sum_win=0
        else:
            for i in range(len(code)):
                t=0
                while t<abs(k):
                    idx=(i-1-t)%n
                    sum_win+=code[idx]
                    t+=1
                res[i]=sum_win
                sum_win=0
        
        return res

                    
        