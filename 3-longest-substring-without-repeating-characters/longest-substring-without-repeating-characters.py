class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        ch=set()
        l=0
        max_len=1
        r=0
        while r < len(s):
            while s[r] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            max_len=max(max_len,r-l+1)
            r+=1
        

        return max_len
            


        