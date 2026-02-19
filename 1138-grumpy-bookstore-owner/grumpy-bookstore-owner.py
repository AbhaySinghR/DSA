class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:


        base=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                base+=customers[i]
        

        best_max=float('-inf')
        running_max=0
        for i in range(minutes):
            if grumpy[i]==1:
                running_max+=customers[i]

        best_max=max(running_max,best_max)

        l=0
        r=minutes
        while r<len(grumpy):
            if grumpy[r]==1:
                running_max+=customers[r]
            if grumpy[l]==1:
                running_max-=customers[l]

            l+=1
            r+=1
            best_max=max(best_max,running_max)
        
        return base+best_max

        