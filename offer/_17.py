from LeetcodeAlgorithm.ListNode import ListNode


class Solution:
    def mergeTwoSortedLinkedList(self, head1, head2):
        if not head1:
            return head2
        elif not head2:
            return head1

        dummy = ListNode(0)
        new_dummy = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next

        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2

        return new_dummy.next