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

    def level_order_traversal(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            print(f"Currently traversed levels: {levels}.")
            if len(levels) == level:
                levels.append([])
            print(f"Current value: {node.val} push to level {level}.")
            levels[level].append(node.val)

            if node.left:
                print(
                    f"Traversing left tree of root node: {node.left.val}. Next level is: {level + 1}.\n"
                )
                helper(node.left, level + 1)
            if node.right:
                print(
                    f"Traversing right tree of root node: {node.right.val}. Next level is: {level + 1}.\n"
                )
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


_root = TreeNode("F")
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

_root.left = b
_root.right = g
_root.left.left = a
_root.left.right = d
_root.left.right.left = c
_root.left.right.right = e
_root.right.right = i
_root.right.right.left = h

_root.print_tree()

tree = TreeNode()
print(f"Level order traversal: {tree.level_order_traversal(root=_root)}.")

"""
Output:
               F
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       B               G
   /¯¯¯ ¯¯¯\            ¯¯¯\
   A       D               I
         /¯ ¯\           /¯
         C   E           H
Currently traversed levels: [].
Current value: F push to level 0.
Traversing left tree of root node: B. Next level is: 1.

Currently traversed levels: [['F']].
Current value: B push to level 1.
Traversing left tree of root node: A. Next level is: 2.

Currently traversed levels: [['F'], ['B']].
Current value: A push to level 2.
Traversing right tree of root node: D. Next level is: 2.

Currently traversed levels: [['F'], ['B'], ['A']].
Current value: D push to level 2.
Traversing left tree of root node: C. Next level is: 3.

Currently traversed levels: [['F'], ['B'], ['A', 'D']].
Current value: C push to level 3.
Traversing right tree of root node: E. Next level is: 3.

Currently traversed levels: [['F'], ['B'], ['A', 'D'], ['C']].
Current value: E push to level 3.
Traversing right tree of root node: G. Next level is: 1.

Currently traversed levels: [['F'], ['B'], ['A', 'D'], ['C', 'E']].
Current value: G push to level 1.
Traversing right tree of root node: I. Next level is: 2.

Currently traversed levels: [['F'], ['B', 'G'], ['A', 'D'], ['C', 'E']].
Current value: I push to level 2.
Traversing left tree of root node: H. Next level is: 3.

Currently traversed levels: [['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E']].
Current value: H push to level 3.
Level order traversal: [['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E', 'H']].


Time Complexity: O(n)
Space Complexity: O(n)
"""
