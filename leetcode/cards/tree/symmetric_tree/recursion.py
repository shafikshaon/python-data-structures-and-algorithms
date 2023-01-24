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

    def print_stack(self, stack):
        return [i.val if i else None for i in stack]

    def symmetric_tree(self, root):
        def is_symmetric(left, right):
            if left:
                print(f"Current left is: {left.val}.")
            if right:
                print(f"Current right is: {right.val}.")
            if not (left or right):
                return True
            elif not (left and right):
                print(
                    f"The left value: {left.val} and right value: {right.val}. One of the value is missing. So return False."
                )
                return False
            elif left.val != right.val:
                print(
                    f"The left value: {left.val} and right value: {right.val}. Both values are not same. So return False."
                )
                return False
            return is_symmetric(left.left, right.right) and is_symmetric(
                left.right, right.left
            )

        return is_symmetric(root, root)


_root = TreeNode("1")
_root.left = TreeNode("2")
_root.right = TreeNode("2")
_root.left.left = TreeNode("3")
_root.left.right = TreeNode("4")
_root.right.left = TreeNode("4")
_root.right.right = TreeNode("3")

_root.print_tree()

tree = TreeNode()
print(f"Is symmetric?: {tree.symmetric_tree(root=_root)}.")

"""
Output:

       1
   /¯¯¯ ¯¯¯\
   2       2
 /¯ ¯\   /¯ ¯\
 3   4   4   3
Current left is: 1.
Current right is: 1.
Current left is: 2.
Current right is: 2.
Current left is: 3.
Current right is: 3.
Current left is: 4.
Current right is: 4.
Current left is: 2.
Current right is: 2.
Current left is: 4.
Current right is: 4.
Current left is: 3.
Current right is: 3.
Is symmetric?: True.


Time Complexity: O(n)
Space Complexity: O(n)
"""
