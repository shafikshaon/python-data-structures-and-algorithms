from typing import List

from linked_list import LinkedList, Node


def create_linked_list(head: List) -> Node | None:
    linked_list1 = LinkedList()
    linked_list1.create_linked_list(head)
    print(f"Linked list 1: {LinkedList.display_by_node(linked_list1.head)}.")
    head = linked_list1.head
    fast = slow = head
    if head is None:
        return None
    while fast.next and fast.next.next:
        print(f"First pointer: {fast.data}, slow pointer: {slow.data}.")
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


print(create_linked_list(head=[3, 2, 0, -4]))

# Output
"""

"""

# Time complexity - O(n)
# Space complexity - O(1)
