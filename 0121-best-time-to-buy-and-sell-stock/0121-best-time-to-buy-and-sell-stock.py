class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p=0
        start=0
        for i in range(start+1,len(prices)):
            if prices[i]<prices[start]:
                start=i
            else:
                max_p=max(max_p,prices[i]-prices[start])
        
        return max_p





        