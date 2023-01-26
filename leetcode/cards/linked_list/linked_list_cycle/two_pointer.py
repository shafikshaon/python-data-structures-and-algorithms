from typing import List

from linked_list import LinkedList


def create_linked_list(head: List) -> bool:
    linked_list1 = LinkedList()
    linked_list1.create_linked_list(head)
    print(f"Linked list 1: {LinkedList.display_by_node(linked_list1.head)}.")
    head = linked_list1.head
    fast = slow = head
    while fast and fast.next:
        print(f"First pointer: {fast.data}, slow pointer: {slow.data}.")
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


create_linked_list(head=[3, 2, 0, -4])

# Output
"""
Linked list 1:   |  3  |  2  |  0  |  -4  |.
First pointer: 3, slow pointer: 3.
First pointer: 0, slow pointer: 2.
"""

# Time complexity - O(n)
# Space complexity - O(1)
