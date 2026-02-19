class Solution:
    def totalFruit(self, fruits: List[int]) -> int:



        hmap={}

        l,r=0,0
        max_fruits=float('-inf')
        while r<len(fruits):

            hmap[fruits[r]]=r

            while len(hmap)>2:
                a = min(hmap, key=hmap.get)
                temp = hmap[a]
                del hmap[a]
                l=temp+1

            
            max_fruits=max(max_fruits,r-l+1)
            r+=1
        return max_fruits
        