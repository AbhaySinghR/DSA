class Solution:
    def longestPalindrome(self, s: str) -> str:

        odd_p=''
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                a=s[l:r+1]
                if len(a)>len(odd_p):
                    odd_p=s[l:r+1]
                l-=1
                r+=1

        even_p=''
        for i in range(len(s)):
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                a=s[l:r+1]
                if len(a)>len(even_p):
                    even_p=s[l:r+1]
                l-=1
                r+=1
        
        if len(odd_p)>len(even_p):
            return odd_p
        return even_p




        