class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i=0
        j=i+1
        max_p=0
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
            else:
                max_p=max(max_p,prices[j]-prices[i])

            j+=1
        
        return max_p

        