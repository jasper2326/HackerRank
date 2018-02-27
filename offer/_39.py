class Solution:
    def getDepth(self, root):
        if not root:
            return 0

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        return max(left, right) + 1


    def getMinDepth(self, root):
        return self.find(root)

    def find(self, root):
        if not root:
            return 0

        left, right = 0, 0
        if root.left:
            left = self.find(root.left)
        else:
            return self.find(root.right) + 1

        if root.right:
            right = self.find(root.right)
        else:
            return left + 1

        return min(left, right) + 1



    def isBalance(self, root):
        balanced, _ = self.validate(root)
        return balanced


    def validate(self, root):
        if not root:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0

        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1



    def isBalanced_1(self, root):
        return self.validate


    def maxDepth(self, root):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1