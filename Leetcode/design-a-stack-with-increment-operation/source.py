class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        x = self.stack.pop()
        return x

    def increment(self, k: int, val: int) -> None:
        for idx in range(len(self.stack)):
            if idx >= k:
                break
            self.stack[idx] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
