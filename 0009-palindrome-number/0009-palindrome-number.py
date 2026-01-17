class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        
        n=str(x)
        if n==n[::-1]:
            return True
        return False

    