class Solution:
    def implementQueue(self):
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def addElement(data, stack1, stack2):
            self.stack1.append(data)

        def deleteElement(stack1, stack2):
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop(-1))
            if not self.stack2:
                return None

            return self.stack2.pop(-1)