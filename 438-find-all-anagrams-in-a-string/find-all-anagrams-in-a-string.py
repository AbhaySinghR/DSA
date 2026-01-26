class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        idx=[]
        i=0
        j=len(p)-1
        p=''.join(sorted(p))
        while j<len(s):
            if j==len(s)-1:
                new_str=s[i:]
                new_str=''.join(sorted(new_str))    
            else:
                new_str=s[i:j+1]
                new_str=''.join(sorted(new_str))
            if new_str==p:
                idx.append(i)
            i+=1
            j+=1
        
        return idx



        