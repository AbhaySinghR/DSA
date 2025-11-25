class Solution:
    def isPalindrome(self, x: int) -> bool:


        if x>0:
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
        elif x==0:
            return True
        else:
            return False


        