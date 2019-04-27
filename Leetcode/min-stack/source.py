class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min is None or self.min > x:
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            del self.stack[-1]
            self.min = None
        for i in self.stack:
            if self.min is None or self.min > i:
                self.min = i

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
