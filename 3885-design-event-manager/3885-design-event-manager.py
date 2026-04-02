class EventManager:

    def __init__(self, events: list[list[int]]):


        self.heap = []
        self.hmap={}

        for eid, p in events:
            heapq.heappush(self.heap,(-p,eid))
            self.hmap[eid]=p
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:

        self.hmap[eventId]=newPriority
        heapq.heappush(self.heap,(-newPriority,eventId))
        
    def pollHighest(self) -> int:

        while self.heap:
            p,eid=heapq.heappop(self.heap)
            if eid in self.hmap and self.hmap[eid]==-p:
                del self.hmap[eid]
                return eid
        return -1
                
        
            
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()