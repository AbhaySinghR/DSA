class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap={}
        for i in range(len(strs)):
            s=''.join(sorted(strs[i]))
            if s not in hmap:
                hmap[s]=[]
            hmap[s].append(strs[i])
        
        final_li=[]
        for j in hmap.values():
            final_li.append(j)
        
        return final_li
        