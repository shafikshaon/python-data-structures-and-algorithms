from typing import List

from linked_list import LinkedList, Node


def create_linked_list(head: List) -> None:
    linked_list = LinkedList()
    linked_list.create_linked_list(head)
    print(f"The initial linked list: {linked_list.display()}.")
    head = linked_list.head

    def reverse_list(head):
        if not head or not head.next:
            return head
        p = reverse_list(head.next)
        head.next.next = head
        head.next = None
        print(f"Linked list at this stage: {LinkedList.display_by_node(p)}")
        return p

    head = reverse_list(head)
    print(f"\nReversed linked list: {LinkedList.display_by_node(head)}")


create_linked_list(head=[1, 2, 3])

# Output
"""
The initial linked list: 1, 2, 3.
Linked list at this stage:   |  3  |  2  |
Linked list at this stage:   |  3  |  2  |  1  |

Reversed linked list:   |  3  |  2  |  1  |
"""

# Time complexity - O(n)
# Space complexity - O(n)
