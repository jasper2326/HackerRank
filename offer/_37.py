class Solution:
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next

        while nodeB:
            lenB += 1
            nodeB = nodeB.next

        node1, node2 = headA, headB
        
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -= 1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1