class Solution:
    def postOrderTraversal(self, root):
        self.result = []
        self.traverse(root)
        return self.result


    def traverse(self, root):
        if not root:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.result.append(root.val)


    def postOrderTraversal_1(self, root):
        self.result_1 = []
        self.stack = []
        prev = None
        curr = root

        if not root:
            return self.result_1
        self.stack.append(root)

        while self.stack:
            curr = self.stack.pop()
            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left:
                    self.stack.append(curr.left)
                elif curr.right:
                    self.stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    self.stack.append(curr.right)
            else:
                self.result_1.append(curr.val)
                self.stack.pop()

            prev = curr

        return self.result_1