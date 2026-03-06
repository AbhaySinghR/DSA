class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions=sorted(potions)
        n=len(spells)
        m=len(potions)
        li=[]
        for i in range(n):
            l=0
            r=m-1
            cnt=0
            req=success/spells[i]
            while l<=r:
                mid=(l+r)//2
                if potions[mid]>=req:
                    cnt=m-mid
                    r=mid-1
                else:
                    l=mid+1
            li.append(cnt)
        
        return li

