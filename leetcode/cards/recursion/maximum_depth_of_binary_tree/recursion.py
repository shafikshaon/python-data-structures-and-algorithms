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

    def max_depth(self, root):
        if not root:
            return 0
        else:
            print(f"Current node is: {root.val}.")
            print(
                f"Finding max height of left node: {root.left.val if root.left else None} and root is {root.val}."
            )
            left_height = self.max_depth(root.left)
            print(f"Left height is: {left_height}.\n")
            print(
                f"Finding max height of right node: {root.right.val if root.right else None} and root is {root.val}."
            )
            right_height = self.max_depth(root.right)
            print(f"Right height is: {right_height}.\n")
            print(f"Current max depth is: {max(left_height, right_height) + 1}.")
            return max(left_height, right_height) + 1


_root = TreeNode("3")
a = TreeNode("9")
b = TreeNode("20")
c = TreeNode("15")
d = TreeNode("7")

_root.left = a
_root.right = b
_root.right.left = c
_root.right.right = d

_root.print_tree()

tree = TreeNode()
print(f"Max depth: {tree.max_depth(root=_root)}.")

"""
Output:

       3
   /¯¯¯ ¯¯¯\
   9      20
         /¯ ¯\
        15   7
Current node is: 3.
Finding max height of left node: 9 and root is 3.
Current node is: 9.
Finding max height of left node: None and root is 9.
Left height is: 0.

Finding max height of right node: None and root is 9.
Right height is: 0.

Current max depth is: 1.
Left height is: 1.

Finding max height of right node: 20 and root is 3.
Current node is: 20.
Finding max height of left node: 15 and root is 20.
Current node is: 15.
Finding max height of left node: None and root is 15.
Left height is: 0.

Finding max height of right node: None and root is 15.
Right height is: 0.

Current max depth is: 1.
Left height is: 1.

Finding max height of right node: 7 and root is 20.
Current node is: 7.
Finding max height of left node: None and root is 7.
Left height is: 0.

Finding max height of right node: None and root is 7.
Right height is: 0.

Current max depth is: 1.
Right height is: 1.

Current max depth is: 2.
Right height is: 2.

Current max depth is: 3.
Max depth: 3.


Time Complexity: O(n)
Space Complexity: O(log(n))
In the worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N)). Therefore, the space complexity in this case would be O(log(N).
"""
