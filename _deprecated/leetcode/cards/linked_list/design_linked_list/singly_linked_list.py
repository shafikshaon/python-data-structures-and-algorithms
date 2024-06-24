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

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


obj = MyLinkedList()
param_1 = obj.get(2)
print(f"Value from index 2: {param_1}.")
obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
obj.addAtTail(6)
obj.addAtIndex(5, 5)
obj.deleteAtIndex(2)
param_1 = obj.get(2)
print(f"Value from index 2: {param_1}.")
obj.printList()

"""
Output:
Value from index: -1.
Value from index: 4.
1
2
4
6
5
"""
