class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        li=s.split(' ')
        i=len(li)-1
        while i>=0:
            if li[i] not in [' ','']:
                res=len(li[i])
                break
            i-=1
        
        return res
        