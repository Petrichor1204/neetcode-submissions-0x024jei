class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()
        
    def top(self) -> int:
        top_element = self.stack[-1]
        return top_element
        
    def getMin(self) -> int:
        return self.min_stack[-1]

