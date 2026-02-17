class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


        people.sort()
        i,w_sum=0,0
        cnt=0
        j=len(people)-1
        while i<=j:
            if i==j and people[i]<=limit:
                cnt+=1
                break
            w_sum=people[i]+people[j]
            if w_sum <=limit:
                cnt+=1
                i+=1
                j-=1
            else:
                cnt+=1
                j-=1
        return cnt
            


        