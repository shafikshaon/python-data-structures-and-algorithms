from typing import List

from linked_list import LinkedList, Node


def create_linked_list(list1: List, list2: List) -> Node:
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    linked_list1.create_linked_list(list1)
    linked_list2.create_linked_list(list2)
    print(f"Linked list 1: {LinkedList.display_by_node(linked_list1.head)}.")
    print(f"Linked list 2: {LinkedList.display_by_node(linked_list2.head)}.")

    list1 = linked_list1.head
    list2 = linked_list2.head

    temp = Node(None)
    current = temp

    while list1 and list2:
        print("\n")
        print(f"List 1: {LinkedList.display_by_node(list1)}")
        print(f"List 2: {LinkedList.display_by_node(list2)}")
        print(f"Sorted list: {LinkedList.display_by_node(temp)}\n")
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next
    current.next = list1 or list2
    print(f"Linked list: {LinkedList.display_by_node(temp.next)}.")
    return temp.next


create_linked_list(list1=[1, 2, 4], list2=[1, 3, 4])

# Output
"""
Linked list 1:   |  1  |  2  |  4  |.
Linked list 2:   |  1  |  3  |  4  |.


List 1:   |  1  |  2  |  4  |
List 2:   |  1  |  3  |  4  |
Sorted list:   |  None  |



List 1:   |  1  |  2  |  4  |
List 2:   |  3  |  4  |
Sorted list:   |  None  |  1  |  3  |  4  |



List 1:   |  2  |  4  |
List 2:   |  3  |  4  |
Sorted list:   |  None  |  1  |  1  |  2  |  4  |



List 1:   |  4  |
List 2:   |  3  |  4  |
Sorted list:   |  None  |  1  |  1  |  2  |  4  |



List 1:   |  4  |
List 2:   |  4  |
Sorted list:   |  None  |  1  |  1  |  2  |  3  |  4  |

Linked list:   |  1  |  1  |  2  |  3  |  4  |  4  |.
"""

# Time complexity - O(n)
# Space complexity - O(1)
