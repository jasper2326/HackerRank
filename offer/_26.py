from offer import RandomListNode


class Solution:
    # Use HashMap to store randomNode
    def copyRandomList(self, head):
        if not head:
            return head

        myMap = {}
        newHead = RandomListNode(head.label)
        myMap[head] = newHead

        p = head
        q = newHead
        while p:
            q.random = p.random
            if p.next:
                q.next = RandomListNode(p.next.label)
                myMap[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next

        p = newHead
        while p:
            if p.random:
                p.random = myMap[p.random]
            p = p.next

        return newHead



    #Duplicate everything then seperate them
    def copyRandomList_1(self, head):
        if not head:
            return head

        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)


    def copyNext(self, head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next


    def copyRandom(self, head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next


    def splitList(self, head):
        newHead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next

        return newHead