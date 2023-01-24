class TreeNode:
    answer = []

    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
                )  # correct the position according to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

    def post_order_traversal(self, node):
        if not node:
            return
        print(f"Traversing left node of root node: {node.val}.")
        self.post_order_traversal(node.left)
        print(f"Traversing right node of root node: {node.val}.")
        self.post_order_traversal(node.right)
        self.answer.append(node.val)
        return self.answer


root = TreeNode("F")
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

root.left = b
root.right = g
root.left.left = a
root.left.right = d
root.left.right.left = c
root.left.right.right = e
root.right.right = i
root.right.right.left = h

root.print_tree()

tree = TreeNode()
print(f"Post order traversal: {tree.post_order_traversal(node=root)}.")

"""
Output:

               F
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       B               G
   /¯¯¯ ¯¯¯\            ¯¯¯\
   A       D               I
         /¯ ¯\           /¯
         C   E           H
Traversing left node of root node: F.
Traversing left node of root node: B.
Traversing left node of root node: A.
Traversing right node of root node: A.
Traversing right node of root node: B.
Traversing left node of root node: D.
Traversing left node of root node: C.
Traversing right node of root node: C.
Traversing right node of root node: D.
Traversing left node of root node: E.
Traversing right node of root node: E.
Traversing right node of root node: F.
Traversing left node of root node: G.
Traversing right node of root node: G.
Traversing left node of root node: I.
Traversing left node of root node: H.
Traversing right node of root node: H.
Traversing right node of root node: I.
Post order traversal: ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'].


Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Algorithm
1. Initialize an empty array answer.
2. Start with the root node root. If root is not NULL:
      i. repeat step 2 with root's left child
     ii. repeat step 2 with root's right child.
    iii. add its value to answer.
3. Return answer after the iteration stops.
"""
