class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)<1:
            return 0
        hmap={}
        i,j=0,0
        max_l=1
        while j < len(s):
            if s[j] in hmap:
                max_l=max(max_l, j-i)
                pos = hmap[s[j]]
                i = pos + 1
            hmap[s[j]]=j
            j+=1
        max_l=max(max_l, j-i)
        return max_l    




        