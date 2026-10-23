# Stack Operations

class MyStack:
    def __init__(self):
        self.stack = []
    # Define your stack

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.isEmpty():
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
