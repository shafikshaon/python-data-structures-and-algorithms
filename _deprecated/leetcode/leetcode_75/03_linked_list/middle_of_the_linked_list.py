from typing import List

from linked_list import LinkedList


def create_linked_list(head: List) -> bool:
    linked_list1 = LinkedList()
    linked_list1.create_linked_list(head)
    print(f"Linked list: {LinkedList.display_by_node(linked_list1.head)}.")
    head = linked_list1.head
    fast = slow = head
    while fast and fast.next:
        print(f"First pointer: {fast.data}, slow pointer: {slow.data}.")
        fast = fast.next.next
        slow = slow.next
    print(f"Linked list: {LinkedList.display_by_node(slow)}.")
    return slow


create_linked_list(head=[1, 2, 3, 4, 5])
create_linked_list(head=[1, 2, 3, 4, 5, 6])

# Output
"""
Linked list:   |  1  |  2  |  3  |  4  |  5  |.
First pointer: 1, slow pointer: 1.
First pointer: 3, slow pointer: 2.
Linked list:   |  3  |  4  |  5  |.
Linked list:   |  1  |  2  |  3  |  4  |  5  |  6  |.
First pointer: 1, slow pointer: 1.
First pointer: 3, slow pointer: 2.
First pointer: 5, slow pointer: 3.
Linked list:   |  4  |  5  |  6  |.
"""

# Time complexity - O(n)
# Space complexity - O(1)
