class RandomizedSet:

    def __init__(self):

        self.hmap={}
        self.li=[]
        

    def insert(self, val: int) -> bool:

        if val in self.hmap:
            return False
        
        self.li.append(val)
        self.hmap[val]=len(self.li)-1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        
        idx=self.hmap[val]
        self.hmap[self.li[-1]]=idx
        self.li[-1],self.li[idx]=self.li[idx],self.li[-1]
        del self.hmap[val]
        self.li.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.li))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()