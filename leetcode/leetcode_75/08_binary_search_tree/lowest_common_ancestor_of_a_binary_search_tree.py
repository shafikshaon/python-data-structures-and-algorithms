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

    def is_valid_bst(self):
        root = self
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.data <= prev:
                return False
            prev = root.data
            root = root.right
        return True

    def lowest_common_ancestor(self, p, q):
        p_val = p.data
        q_val = q.data
        print(f'"p" value is: {p_val}.')
        print(f'"q" value is: {q_val}.')

        node = self

        # Traverse the tree
        while node:
            # Value of current node or parent node
            parent_val = node.data
            print(f"Current node value: {parent_val}.")

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                print(
                    f"p and q value greater that parent node. {p_val} > {parent_val} and {q_val} > {parent_val}."
                )
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                print(
                    f"p and q value lesser that parent node. {p_val} < {parent_val} and {q_val} < {parent_val}."
                )
                node = node.left
            else:
                print(f"Now lowest common ancestor found. The value is: {node.data}.")
                return node


root = Node(6)
two = Node(2)
eight = Node(8)
root.left = two
root.right = eight

zero = Node(0)
four = Node(4)
seven = Node(7)
nine = Node(9)

root.left.left = zero
root.left.right = four
root.right.left = seven
root.right.right = nine

three = Node(3)
five = Node(5)
root.left.right.left = three
root.left.right.right = five

root.print_tree()

print(f"Is Valid BST?: {root.is_valid_bst()}")
lowest_common_ancestor = root.lowest_common_ancestor(root.left, root.left.right)
print(f"Lowest Common Ancestor: {lowest_common_ancestor.data}")

# Input: [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
               6
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       2               8
   /¯¯¯ ¯¯¯\       /¯¯¯ ¯¯¯\
   0       4       7       9
         /¯ ¯\
         3   5
Is Valid BST?: True
"p" value is: 2.
"q" value is: 4.
Current node value: 6.
p and q value lesser that parent node. 2 < 6 and 4 < 6.
Current node value: 2.
Now lowest common ancestor found. The value is: 2.
Lowest Common Ancestor: 2
"""
