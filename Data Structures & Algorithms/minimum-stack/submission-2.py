class MinStack:

    def __init__(self):
        self.stack = []
        self.sort = []

    def push(self, val: int) -> None:
        if self.sort == [] or self.stack == []:
            self.sort.append(val)
        else:
            self.sort.append(min(val, self.sort[-1]))
        self.stack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.sort.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sort[-1]
        
        
