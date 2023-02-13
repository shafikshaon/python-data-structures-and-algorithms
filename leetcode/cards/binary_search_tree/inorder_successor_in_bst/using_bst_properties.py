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

    def inorder_successor(self, p):
        root = self
        successor = None
        while root:
            print(f"p = {p.data}. root = {root.data}.")
            if p.data >= root.data:
                print(
                    f"p({p.data}) value greater than root({root.data if root else None}) value. So new root is right."
                )
                root = root.right
            else:
                print(
                    f"p({p.data}) value less than root({root.data if root else None}) value. "
                    f"So new root is left. Successor: {successor.data if successor else None}."
                )
                successor = root
                root = root.left
            print(f"New root is: {root.data if root else None}.")
        return successor


# Use the insert method to add nodes
root = Node(2)
left = Node(1)
right = Node(3)
root.left = left
root.right = right

p = Node(1)
root.print_tree()
successor = root.inorder_successor(p=p)
print(f"\nSuccessor: {successor.data}")

# root = [2,1,3], p = 1
# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
   2
 /¯ ¯\
 1   3
p = 1. root = 2.
p(1) value less than root(2) value. So new root is left. Successor: None.
Now root is: 1.
p = 1. root = 1.
p(1) value greater than root(1) value. So new root is right.
New root is: None.

Successor: 2
"""
