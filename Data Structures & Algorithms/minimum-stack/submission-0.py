class MinStack:

    def __init__(self):
        self.l = []
        self.cur_min = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.cur_min: self.cur_min.append(val)
        else: self.cur_min.append(min(self.cur_min[-1], val))

    def pop(self) -> None:
        self.l.pop()
        self.cur_min.pop()

    def top(self) -> int:
        return self.l[-1]        

    def getMin(self) -> int:
        return self.cur_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()