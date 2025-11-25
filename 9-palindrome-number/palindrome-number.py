class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        r=''
        i=len(s)-1
        while i>=0:
            r=r+s[i]
            i-=1
        if r==s:
            return True
        else:
            return False
        

    