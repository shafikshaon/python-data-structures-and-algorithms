class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def is_valid_bst(self):
        root = self
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                print(f"Add {root.data} in stack.")
                stack.append(root)
                root = root.left
            print(f"Current stack is: {[d.data for d in stack]}.")
            root = stack.pop()
            print(f"Current root value is: {root.data}.")
            if root.data <= prev:
                print(
                    f"Comparing current value {root.data} and previous value {prev}. {root.data} <= {prev}.\n"
                )
                return False
            prev = root.data
            print(f"Now previous value is: {prev}.")
            root = root.right
            print(f"Current root (right) value is: {root.data if root else None}.\n")
        return True


# Use the insert method to add nodes
root = Node(5)
left = Node(1)
right = Node(4)
root.left = left
root.right = right

three = Node(3)
six = Node(6)

root.right.left = three
root.right.right = six

root.print_tree()

print(f"Is Valid BST?: {root.is_valid_bst()}")

# Input: root = [5,1,4,null,null,3,6]
# Time complexity: O(n)
# Space complexity: O(n)

# Output
"""
1
5
3
4
6
Add 5 in stack.
Add 1 in stack.
Current stack is: [5, 1].
Current root value is: 1.
Now previous value is: 1.
Current root (right) value is: None.

Current stack is: [5].
Current root value is: 5.
Now previous value is: 5.
Current root (right) value is: 4.

Add 4 in stack.
Add 3 in stack.
Current stack is: [4, 3].
Current root value is: 3.
Comparing current value 3 and previous value 5. 3 <= 5.

Is Valid BST?: False
"""
