class Solution:
    def subtree(self, source, target):
        if not target:
            return True
        if not source:
            return False
        return self.isEqual(source, target) or self.subtree(source.left, target) or self.subtree(source.right, target)

    def isEqual(self, source, target):
        if not source or not target:
            return source == target
        if source.val != target.val:
            return False
        return self.isEqual(source.left, target.left) and self.isEqual(source.right, target.right)
