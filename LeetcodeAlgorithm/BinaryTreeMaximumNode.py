class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # Write your code here
        if not root:
            return root

        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.val > b.val:
            return a
        else:
            return b