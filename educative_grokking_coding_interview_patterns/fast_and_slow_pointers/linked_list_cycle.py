# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # returns the number of nodes in the linked list
    def get_length(self, head):
        temp = head
        length = 0
        while (temp):
            length += 1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    i = 0

    while temp and i < 7:
        if i == 0:
            print("\t", temp.data, end=" ")  # print node value
        else:
            print(temp.data, end=" ")  # print node value
        temp = temp.next
        if i == 6:
            print("(...)")
            break
        if temp:
            print("→ ", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ NULL", end=" ")
        i += 1


def detect_cycle(head):
    slow, fast = head, head
    i, j = 0, 0
    space1, space2, last = 0, 2, 5
    print("\tHead pointer:", head.data)
    print("\tSlow pointer:", slow.data)
    print("\tFast pointer:", fast.data)
    print_list_with_forward_arrow(head)
    print("\n\t", "  " * ((6 * i)) + "ŝf̂")
    # Run the loop until we reach the end of the
    # linked list or find a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        last -= 2

        print("\n\tLoop index:", i)
        i += 1
        j += 2
        # Break the loop if fast pointer has reached at
        # the end of linked list
        if fast is None:
            print("\tSlow pointer:", slow.data)
            print("\tFast pointer: NULL")
            print("\tFast pointer has reached the end"
                  " of the linked list.")
            break
        else:
            print("\tSlow pointer:", slow.data)
            print("\tFast pointer:", fast.data, "\n")
            print_list_with_forward_arrow(head)
        if slow == fast:
            print("\n\t", " " * ((6 * i - 5)), "ŝf̂", sep=" ")
            print("\tBoth slow and fast pointers are pointing"
                  " to the same node!")
            return True
        else:
            if last == -1:
                print("\n\t", " " * ((6 * (space2 - 1)) - ((6 * space1) - 1) - 3),
                      " f̂ast  ", " " * (((6 * i) - 14)), "ŝlow", sep="")
                space2 += 2
            if last == -3:
                print("\n\t", " " * ((6 * (space2 - 1)) - ((6 * space1) - 1) - 5),
                      " f̂ast  ", " " * (((6 * i) - 12) - 16), "ŝlow", sep="")
                space2 += 2
            if last > 0:
                print("\n\t", " " * (6 * i - (i - 1)) + "ŝlow", " " * ((6 * (j - 1)) - ((6 * i))),
                      " f̂ast", sep="")
    return False


def main():
    input = (
        [2, 4, 6, 8, 10, 12],
        [1, 3, 5, 7, 9, 11],
        [0, 1, 2, 3, 4, 6],
        [3, 4, 7, 9, 11, 17],
        [5, 1, 4, 9, 2, 3],
    )
    pos = [0, -1, 1, -1, 2]
    j = 1

    for i in range(len(input)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        if pos[i] != -1:
            length = input_linked_list.get_length(input_linked_list.head)
            last_node = input_linked_list.get_node(input_linked_list.head, length - 1)
            last_node.next = input_linked_list.get_node(input_linked_list.head, pos[i])

        print(f"{j}.\tInput: ")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tProcessing...")
        print(f"\n\tDetected cycle = {detect_cycle(input_linked_list.head)}")
        j += 1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()

# Time complexity - O(n)
# Space complexity - O(1)
