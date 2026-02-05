class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        hmap={}
        cnt=0
        for i in range(len(s)):
            hmap[s[i]]=i
            if len(hmap)==3:
                cnt+=1+ min(hmap['a'],hmap['b'],hmap['c'])
            
        return cnt
        