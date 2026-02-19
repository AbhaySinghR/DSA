class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)==0:
            return 0
        hmap={}
        l,r=0,0
        max_len=float('-inf')
        while r<len(s):

            if s[r] in hmap:
                pos=hmap[s[r]]
                while l<=pos:
                    del hmap[s[l]]
                    l+=1
            
            hmap[s[r]]=r
            max_len=max(max_len,r-l+1)
            r+=1
        
        return max_len

            


        