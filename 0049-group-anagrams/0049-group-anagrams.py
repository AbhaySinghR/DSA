class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hmap={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in hmap:
                hmap[s]=[]
            hmap[s].append(i)
        
        li=[]
        for j in hmap.values():
            li.append(j)
        
        return li
        