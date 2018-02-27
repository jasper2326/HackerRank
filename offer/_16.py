from LeetcodeAlgorithm.ListNode import ListNode


class Solution:
    def reverseLinkedList(self, head):
        current = None
        while head:
            temp = head.next
            head.next = current
            current = head
            head = temp
        return current