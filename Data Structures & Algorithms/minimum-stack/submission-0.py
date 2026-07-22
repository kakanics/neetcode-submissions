class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not len(self.mins):
            self.mins.append(val)
            return
        self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.arr.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]
