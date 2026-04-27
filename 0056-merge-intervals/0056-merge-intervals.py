class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged=True
        while merged:
            merged=False
            i=0
            while i < len( intervals):
                j=i+1
                while j < len(intervals):
                    if intervals[i][1] >= intervals[j][0] and intervals [j][1]>= intervals[i][0]:
                        intervals[i][0]= min(intervals[i][0], intervals[j][0])
                        intervals[i][1]= max(intervals[i][1], intervals[j][1])

                        intervals.pop(j)
                        merged=True
                    else:
                        j=j+1
            
                i=i+1
        
        return intervals 


        
        