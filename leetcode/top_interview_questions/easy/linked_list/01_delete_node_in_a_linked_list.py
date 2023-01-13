from linked_list import LinkedList


def delete_node(temp):
    print(f"Current node: {temp.data} which will be deleted.")
    next_node = temp.next
    if next_node:
        print(f"Current next node is: {temp.data} => {next_node.data}.")
    else:
        print("We are in last node.")
        return

    print(
        f"Updating temp.data = next_node.data ({temp.data} = {next_node.data}). Now {temp.data} replaced by {next_node.data}."
    )
    temp.data = next_node.data
    print(f"Node {temp.data} point to node {next_node.next.data}.")

    temp.next = next_node.next
    print(
        f"Unlink deleted node ({next_node.data}) which was pointed to {next_node.data}."
    )
    next_node.next = None

    del next_node


def create_linked_list(head, node):
    linked_list = LinkedList()
    linked_list.create_linked_list(head)
    print(f"The initial linked list: {linked_list.display()}.")

    temp = linked_list.head
    while temp:
        temp = temp.next
        if temp and temp.data == node:
            delete_node(temp)

    print(f"After delete node {node} the linked list is: {linked_list.display()}.")


create_linked_list(head=[4, 5, 1, 9], node=5)

# Time complexity - O(1)
# Space complexity - O(1)
