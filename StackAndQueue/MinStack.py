# -*- coding: utf-8 -*-


class MinStack:
    def __init__(self):
        """
        Complexity:
            time: O(1)
            space: O(n)
        """
        self.stack = []
        self.minStack = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minStack.append(min(x, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()