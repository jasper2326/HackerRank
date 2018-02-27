class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        result = []
        path = []
        self.dfs(root, target, result, path, 0)
        return result


    def dfs(self, root, target, result, path, sum):
        if not root:
            return

        path.append(root.val)
        sum += root.val

        if not root.left and not root.right and sum == target:
            result.append(path[:])

        if root.left:
            self.dfs(root.left, target, result, path, sum)
        if root.right:
            self.dfs(root.right, target, result, path, sum)
        path.pop()


