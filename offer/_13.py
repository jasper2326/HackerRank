class Solution:
    def deleteNode(self, head, node):
        if head is None or node is None:
            return head
        if head == node:
            return head.next

        if node.next is None:
            dummy = head
            while dummy.next != node:
                dummy = dummy.next
            dummy.next = None
        else:
            node.next = node.next.next
        return head