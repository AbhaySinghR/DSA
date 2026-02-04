class RideSharingSystem:

    def __init__(self):

        self.rider=deque()
        self.driver=deque()
        self.match=set()
        
    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
        self.match.add(riderId)
        

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:

        while self.rider and self.rider[0] not in self.match:
            self.rider.popleft()

        if not self.driver or not self.rider:
            return [-1,-1]

        r=self.rider.popleft()
        d=self.driver.popleft()
        self.match.remove(r)
        return [d,r]
        
        

        

    def cancelRider(self, riderId: int) -> None:
        self.match.discard(riderId)

        
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)