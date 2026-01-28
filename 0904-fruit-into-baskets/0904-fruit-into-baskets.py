class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        max_len=0
        hmap={}
        l,r=0,0
        while r<len(fruits):
            hmap[fruits[r]]=r
            
            while len(hmap)>2:
                a = min(hmap, key=hmap.get)
                temp = hmap[a]
                del hmap[a]
                l=temp+1
            
            max_len=max(max_len,r-l+1)
            r+=1
        
        return max_len
        