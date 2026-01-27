class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        best_max_cond=float('-inf')
        base_happy=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                base_happy+=customers[i]
        
        max_cond_happy_cust=0
        for i in range(minutes):
            if grumpy[i]==1:
                max_cond_happy_cust+=customers[i]
            
        best_max_cond=max(max_cond_happy_cust,best_max_cond)
        l=0
        r=minutes
        while r<len(customers):
            if grumpy[r]==1:
                max_cond_happy_cust+=customers[r]
            if grumpy[l]==1:
                max_cond_happy_cust-=customers[l]
            
            l+=1
            r+=1
            best_max_cond=max(max_cond_happy_cust,best_max_cond)

        return base_happy+best_max_cond
        