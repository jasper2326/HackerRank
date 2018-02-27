class Solution:
    def printFromTop2Bottom(self, root):
        result = []
        if not root:
            return result

        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        return result