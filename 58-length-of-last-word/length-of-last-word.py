class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        cnt=0
        while i>=0:
            if s[i]!=' ':
                break
            i-=1
        while i>=0:
            if s[i]!=' ':
                cnt+=1
            else:
                break
            i-=1
    
        return cnt

