class Node:
    def __init__(self, data):
        self.prev = None
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

        q = [(root, 0, width, "c")]
        levels = []

        while q:
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, "l"))
                q.append((node.right, level + 1, x + seg, "r"))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ""
            pstr = ""
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].data)
                if n[3] == "r":
                    linestr += (
                        " " * (n[2] - preline - 1 - seg - seg // 2)
                        + "¯" * (seg + seg // 2)
                        + "\\"
                    )
                    preline = n[2]
                if n[3] == "l":
                    linestr += " " * (n[2] - preline - 1) + "/" + "¯" * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += (
                    " " * (n[2] - pre - len(valstr)) + valstr
                )  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

    def is_valid_bst(self):
        root = self

        def in_order(root):
            if not root:
                return True
            if not in_order(root.left):
                return False
            if root.data <= self.prev:
                return False
            self.prev = root.data
            return in_order(root.right)

        self.prev = float("-inf")
        return in_order(root)


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
       5
   /¯¯¯ ¯¯¯\
   1       4
         /¯ ¯\
         3   6
Is Valid BST?: False
"""
