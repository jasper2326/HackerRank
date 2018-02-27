from offer.DoublyListNode import DoublyListNode


class Solution:
    def BST2DoublyList(self, root):
        dfs = []
        self.getDFS(root, dfs)
        if len(dfs) == 0:
            return None

        head = None
        prev = None
        for val in dfs:
            node = DoublyListNode(val)
            if head is None:
                head = node
            else:
                prev.next = node
            node.prev = prev
            prev = node
        return head


    def getDFS(self, root, dfs):
        if not root:
            return

        self.getDFS(root.left, dfs)
        dfs.append(root.val)
        self.getDFS(root.right, dfs)
