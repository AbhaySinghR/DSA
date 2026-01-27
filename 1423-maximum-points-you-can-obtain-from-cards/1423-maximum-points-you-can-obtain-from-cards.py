class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        final=0
        max_sum=0
        for i in range(k):
            max_sum+=cardPoints[i]
        final=max(final,max_sum)
        l=k-1
        r=len(cardPoints)-1
        while l>=0:
            max_sum+=cardPoints[r]
            max_sum-=cardPoints[l]
            l-=1
            r-=1
            final=max(final,max_sum)
        
        return final


        