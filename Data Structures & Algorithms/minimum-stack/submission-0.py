class MinStack:

    def __init__(self):
        self.min_stk = deque()
        self.stk = deque()

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.min_stk:
            self.min_stk.append(min(self.min_stk[-1], val))
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.min_stk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
