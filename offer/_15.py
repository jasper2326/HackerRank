class Solution:
    def kthNode(self, head, k):
        fast, slow = head, head
        for i in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow