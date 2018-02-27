class Solution:
    def reflectBinaryTree(self, root):
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.reflectBinaryTree(root.left)
        self.reflectBinaryTree(root.right)