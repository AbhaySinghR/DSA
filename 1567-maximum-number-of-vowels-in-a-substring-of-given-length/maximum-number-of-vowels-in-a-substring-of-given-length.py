class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_len_vow=0
        len_sub_vow=0
        vow_li=['a','e','i','o','u']
        for i in range(k):
            if s[i] in vow_li:
                len_sub_vow+=1
                
        
        max_len_vow=max(max_len_vow,len_sub_vow)
        l=0
        r=k
        while r<len(s):
            if s[r] in vow_li:
                len_sub_vow+=1
            if s[l] in vow_li:
                len_sub_vow-=1
            l+=1
            r+=1
            max_len_vow=max(max_len_vow,len_sub_vow)
            if max_len_vow==k:
                break
            
        
        return max_len_vow


        