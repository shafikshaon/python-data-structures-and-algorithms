class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

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
                valstr = str(n[0].val)
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

    def search_in_binary_tree(self, val):
        root = self

        def search_bst(root, val):
            if not root or val == root.val:
                return root
            return (
                search_bst(root.left, val)
                if root.val > val
                else search_bst(root.right, val)
            )

        return search_bst(root, val)


# Use the insert method to add nodes
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

root.print_tree()
sub_true = root.search_in_binary_tree(val=2)
print(f"\nResulted Tree:")
sub_true.print_tree()

# Input: root = [4,2,7,1,3], val = 2
# Time complexity: O(n)
# Space complexity: O(n)

# Output
"""

       4
   /¯¯¯ ¯¯¯\
   2       7
 /¯ ¯\
 1   3

Resulted Tree:

   2
 /¯ ¯\
 1   3

"""
