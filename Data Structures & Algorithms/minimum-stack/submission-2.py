class MinStack:

    def __init__(self):
        self.stack = []
        self.min_a = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_a = min(self.min_a, val)

    def pop(self) -> None:
        if self.stack:
            last_a = self.stack[-1]
            self.stack.pop()
            if last_a == self.min_a:
                self.min_a = math.inf
                for a in self.stack:
                    self.min_a = min(self.min_a, a)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_a
