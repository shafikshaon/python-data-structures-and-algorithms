from singly_linked_list import *


def main(head, obj):
    print(f"Input linked list: {obj.printList(head)}.\n")

    def swap_pairs(head_node):
        if not head_node or not head_node.next:
            return head_node

        # Nodes to be swapped
        first_node = head_node
        second_node = head_node.next
        print(f"First node: {head_node.val}. Second node: {second_node.val}.")

        # Swapping
        first_node.next = swap_pairs(head_node=second_node.next)
        second_node.next = first_node
        print(
            f"After swapping. First node: {head_node.val}. Second node: {second_node.val}."
        )
        # Now the head is the second node
        return second_node

    print(f"\nFinal linked list: {obj.printList(swap_pairs(head_node=head))}.\n")


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
main(head=obj.head, obj=obj)


"""
Output:
Input linked list: [1, 2, 3, 4].

First node: 1. Second node: 2.
First node: 3. Second node: 4.
After swapping. First node: 3. Second node: 4.
After swapping. First node: 1. Second node: 2.

Final linked list: [2, 1, 4, 3].


Time Complexity: O(n)
Space Complexity: O(n)
"""
