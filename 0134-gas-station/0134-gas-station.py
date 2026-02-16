class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):
            return -1

        start=0
        tc=0
        for i in range(len(gas)):
            tc+=gas[i]-cost[i]
            if tc<0:
                start=i+1
                tc=0
        
        return start
        