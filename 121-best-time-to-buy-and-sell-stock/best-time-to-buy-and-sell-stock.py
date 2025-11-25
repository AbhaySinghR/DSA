class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)==1:
            return 0
        max_p=0
        i=0
        j=i+1
        while j<len(prices):
            if prices[j]<=prices[i]:
                i=j
                j+=1
            elif prices[j]>prices[i]:
                max_p=max(max_p,prices[j]-prices[i])
                j+=1
            
        
        return max_p
            





        