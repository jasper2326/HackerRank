import ListNode


class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        count = 0
        while head.next:
            count += 1
            head = head.next

        return count