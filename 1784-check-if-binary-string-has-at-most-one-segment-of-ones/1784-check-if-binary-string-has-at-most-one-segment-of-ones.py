class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        max_cnt,cnt=0,0
        for i in range(len(s)):
            if s[i]=="1":
                cnt=1
            else:
                max_cnt+=cnt
                cnt=0
        if cnt==1:
            max_cnt+=cnt
        return True if max_cnt<=1 else False




        