class Solution:
    def hIndex(self, citations: List[int]) -> int:
        a=sorted(citations,reverse=True)
        count=0
        for i in range(len(a)):
            if a[i]>=i+1:
                count+=1
        
        return count