class Solution:
    def reversePrint(self, head):
        if head is None:
            return None
        if head.next is None:
            return head.val

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        reversed = stack[::-1]
        for item in reversed:
            print(item)