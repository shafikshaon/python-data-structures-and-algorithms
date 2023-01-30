class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            prev = self.head
            new_node = ListNode(val)

            if prev:
                if index == 0:
                    self.head = new_node
                    new_node.next = prev
                else:
                    for i in range(index - 1):
                        prev = prev.next
                    new_node.next = prev.next
                    prev.next = new_node
            else:
                self.head = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            prev = self.head
            if index == 0:
                self.head = prev.next
            else:
                for i in range(index - 1):
                    prev = prev.next
                if not prev.next:
                    self.head = None
                prev.next = prev.next.next
            self.size -= 1

    def printList(self, head):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
