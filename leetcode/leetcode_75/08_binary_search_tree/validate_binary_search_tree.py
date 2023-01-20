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
    def print_tree(root):
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        nlevels = height(root)
        width = pow(2, nlevels + 1)

        q = [(root, 0, width, 'c')]
        levels = []

        while (q):
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].data)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

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
