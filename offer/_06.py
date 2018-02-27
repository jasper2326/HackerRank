from offer.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        # write your code here
        if not inorder or not preorder or len(inorder) != len(preorder):
            return None

        root = TreeNode(preorder[0])
        root_position = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + root_position], inorder[ : root_position])
        root.right = self.buildTree(preorder[1 + root_position : ], inorder[root_position + 1 : ])
        return root