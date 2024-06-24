from singly_linked_list import *


def main(head, obj):
    print(f"Input linked list: {obj.printList(head)}.\n")
    temp = ListNode()
    curr = head

    while curr:
        prev = temp
        while prev.next and prev.next.val <= curr.val:
            prev = prev.next

        next = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next
        print(
            f"Prev: {prev.val if prev else None}. Next: {next.val if next else None}. Curr: {curr.val if curr else None}."
        )
        print(f"Now linked list is (head: temp): {obj.printList(temp)}.\n")
    print(f"Output linked list: {obj.printList(temp.next)}.")
    return temp.next


obj = MyLinkedList()
obj.addAtHead(4)
obj.addAtTail(2)
obj.addAtTail(1)
obj.addAtTail(3)
main(head=obj.head, obj=obj)

"""
Output:
Input linked list: [4, 2, 1, 3].

Prev: None. Next: 2. Curr: 2.
Now linked list is (head: temp): [None, 4].

Prev: None. Next: 1. Curr: 1.
Now linked list is (head: temp): [None, 2, 4].

Prev: None. Next: 3. Curr: 3.
Now linked list is (head: temp): [None, 1, 2, 4].

Prev: 2. Next: None. Curr: None.
Now linked list is (head: temp): [None, 1, 2, 3, 4].

Output linked list: [1, 2, 3, 4].


Time complexity: O(n^2)
Space complexity: O(1)
"""
