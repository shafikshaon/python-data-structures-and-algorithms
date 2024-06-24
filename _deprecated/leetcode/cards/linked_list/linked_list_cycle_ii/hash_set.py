from typing import List

from linked_list import LinkedList, Node


def create_linked_list(head: List) -> Node | None:
    linked_list1 = LinkedList()
    linked_list1.create_linked_list(head)
    print(f"Linked list 1: {LinkedList.display_by_node(linked_list1.head)}.")
    head = linked_list1.head

    visited = set()
    node = head

    while node:
        if node in visited:
            print(f"Node {node.data} visited already.")
            return node
        else:
            visited.add(node)
            node = node.next
    return None


print(create_linked_list(head=[3, 2, 0, -4]))

# Output
"""
Linked list 1:   |  3  |  2  |  0  |  -4  |.
None
"""

# Time complexity - O(n)
# Space complexity - O(1)
