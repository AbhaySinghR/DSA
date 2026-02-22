class StockSpanner:

    def __init__(self):

        self.st=[]
        self.val=1
        

    def next(self, price: int) -> int:

        self.val=1
        while self.st and price >=self.st[-1][0]:
            price_prev,val_p=self.st.pop()
            self.val+=val_p
        self.st.append((price,self.val))
        return self.val
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)