import ListNode


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next