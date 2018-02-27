class Solution:
    class stackWithMin:
        def __init__(self):
            self.dataStack = []
            self.minStack = []


        def pop(self):
            if self.dataStack[-1] == self.minStack[-1]:
                self.minStack.pop()
            return self.dataStack.pop()


        def push(self, num):
            self.dataStack.append(num)
            if len(self.minStack) == 0 or self.minStack[-1] >= num:
                self.minStack.append(num)


        def min(self):
            if len(self.minStack) == 0:
                return -1
            return self.minStack[-1]