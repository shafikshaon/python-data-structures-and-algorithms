from typing import List

from linked_list import LinkedList, Node


def merge_two_lists(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1
    elif list1.data < list2.data:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2


def create_linked_list(list1: List, list2: List) -> Node:
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    linked_list1.create_linked_list(list1)
    linked_list2.create_linked_list(list2)
    print(f"Linked list 1: {LinkedList.display_by_node(linked_list1.head)}.")
    print(f"Linked list 2: {LinkedList.display_by_node(linked_list2.head)}.")

    list1 = linked_list1.head
    list2 = linked_list2.head
    print(f"Merged linked list: {LinkedList.display_by_node(merge_two_lists(list1, list2))}")
    return merge_two_lists(list1, list2)


create_linked_list(list1=[1, 2, 4], list2=[1, 3, 4])

# Output
"""
Linked list 1:   |  1  |  2  |  4  |.
Linked list 2:   |  1  |  3  |  4  |.
Merged linked list:   |  1  |  1  |  2  |  3  |  4  |  4  |
"""

# Time complexity - O(n)
# Space complexity - O(n)
