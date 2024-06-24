from typing import List

from linked_list import LinkedList, Node


def create_linked_list(head: List, n: int) -> None:
    linked_list = LinkedList()
    linked_list.create_linked_list(head)
    print(
        f"The initial linked list: {linked_list.display()}. We have to delete nth ({n}) from end."
    )

    temp = Node(0)
    temp.next = linked_list.head

    first = temp
    second = temp

    for i in range(n + 1):
        first = first.next

    while first:
        print(f"First pointer in {first.data} and second pointer in {second.data}.")
        first = first.next
        second = second.next
    print(f"Now pointed {second.data} to {second.next.next.data}.")
    second.next = second.next.next
    print(f"The final linked list is: {LinkedList.display_by_node(temp.next)}.")
    return temp.next


create_linked_list(head=[1, 2, 3, 4, 5], n=2)

"""
Output:
The initial linked list: 1, 2, 3, 4, 5. We have to delete nth (2) from end.
First pointer in 3 and second pointer in 0.
First pointer in 4 and second pointer in 1.
First pointer in 5 and second pointer in 2.
Now pointed 3 to 5.
The final linked list is:   |  1  |  2  |  3  |  5  |.
"""
# Time complexity - O(n)
# Space complexity - O(1)
