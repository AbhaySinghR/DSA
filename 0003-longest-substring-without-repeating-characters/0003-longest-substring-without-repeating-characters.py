class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s)<1:
            return 0
        hmap={}
        i,j=0,0
        max_l=1
        while j < len(s):
            if s[j] in hmap:
                pos=hmap[s[j]]
                while i <=pos:
                    del hmap[s[i]]
                    i+=1
            hmap[s[j]]=j
            max_l=max(max_l,j-i+1)
            j+=1


        return max_l



        