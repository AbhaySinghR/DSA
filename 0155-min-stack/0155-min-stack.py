class MinStack:


    def __init__(self):

        self.st=[]
        self.curr_min=float('inf')
        

    def push(self, val: int) -> None:

        if not self.st:
            self.st.append((val,val))
        else:
            if val < self.st[-1][1]:
                self.st.append((val,val))
            else:
                self.st.append((val,self.st[-1][1]))



    def pop(self) -> None:

        self.st.pop()
        

    def top(self) -> int:

        return self.st[-1][0]
        

    def getMin(self) -> int:

        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()