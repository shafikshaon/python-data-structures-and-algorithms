from singly_linked_list import *


def main(head, obj):
    print(f"Input linked list: {obj.printList(head)}.\n")

    temp = ListNode(-1)
    temp.next = head

    prev_node = temp

    while head and head.next:
        # Nodes to be swapped
        first_node = head
        second_node = head.next
        print(f"First node: {first_node.val}. Second node: {second_node.val}.")

        # Swapping
        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        print(f"Now linked list is: {obj.printList(temp)}.")

        # Reinitializing the head and prev_node for next swap
        prev_node = first_node
        head = first_node.next
    print(f"\nFinal linked list: {obj.printList(temp.next)}.\n")
    # Return the new head node.
    return temp.next


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
main(head=obj.head, obj=obj)

"""
Output:



Time Complexity: O(n)
Space Complexity: O(1)
"""
