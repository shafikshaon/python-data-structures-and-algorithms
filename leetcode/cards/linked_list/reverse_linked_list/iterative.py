from typing import List

from linked_list import LinkedList, Node


def create_linked_list(head: List) -> None:
    linked_list = LinkedList()
    linked_list.create_linked_list(head)
    print(f"The initial linked list: {linked_list.display()}.")
    head = linked_list.head

    prev = None
    current = head

    while current:
        print("\n----------------------------------------------------------")
        print(f"prev node: {prev.data}.")
        print(f"Current node: {current.data}.")
        next_node = current.next
        if next_node:
            print(f"Next node: {next_node.data}.")
        current.next = prev
        prev = current
        current = next_node
        print(f"Linked list at this stage: {LinkedList.display_by_node(prev)}")
    print(f"\nReversed linked list: {LinkedList.display_by_node(prev)}")
    return prev


create_linked_list(head=[1, 2, 3])

# Output
"""
The initial linked list: 1, 2, 3.

----------------------------------------------------------
prev node: None.
Current node: 1.
Next node: 2.
Linked list at this stage:   |  1  |  None  |

----------------------------------------------------------
prev node: 1.
Current node: 2.
Next node: 3.
Linked list at this stage:   |  2  |  1  |  None  |

----------------------------------------------------------
prev node: 2.
Current node: 3.
Linked list at this stage:   |  3  |  2  |  1  |  None  |

Reversed linked list:   |  3  |  2  |  1  |  None  |
"""

# Time complexity - O(n)
# Space complexity - O(1)
