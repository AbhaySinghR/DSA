class Solution:
    def isPalindrome(self, s: str) -> bool:

        ns=''
        for i in s:
            if i.isalnum():
                ns+=i.lower()
        
        i=0
        j=len(ns)-1
        while i<j:
            if ns[i]!=ns[j]:
                return False
            i+=1
            j-=1
        
        return True
