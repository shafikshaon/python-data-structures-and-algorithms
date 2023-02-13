class TreeNode:
    answer = []

    def __init__(self, val=float("-inf"), left=None, right=None):
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
        return [i[0].val if i and i[0] else None for i in stack]

    def has_path_sum(self, root, sum):
        if not root:
            return False
        print(f"\nRoot is: {root.val} and current sum is: {sum}.")
        sum -= root.val
        print(f"Current sum is: {sum}.")
        if not root.left and not root.right:
            return sum == 0
        print(
            f"Left node is: {root.left.val if root.left else 0}. Right node is: {root.right.val if root.right else 0}. Root is: {root.val}."
        )
        return self.has_path_sum(root.left, sum) or self.has_path_sum(root.right, sum)


_root = TreeNode(5)
_root.left = TreeNode(4)
_root.right = TreeNode(8)
_root.left.left = TreeNode(11)
_root.left.left.left = TreeNode(7)
_root.left.left.right = TreeNode(2)

_root.right.left = TreeNode(13)
_root.right.right = TreeNode(4)
_root.right.right.right = TreeNode(1)

_root.print_tree()

tree = TreeNode()
print(f"Has path sum?: {tree.has_path_sum(root=_root, sum=22)}.")

"""
Output:
               5
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       4               8
   /¯¯¯            /¯¯¯ ¯¯¯\
  11              13       4
 /¯ ¯\                      ¯\
 7   2                       1

Root is: 5 and current sum is: 22.
Current sum is: 17.
Left node is: 4. Right node is: 8. Root is: 5.

Root is: 4 and current sum is: 17.
Current sum is: 13.
Left node is: 11. Right node is: 0. Root is: 4.

Root is: 11 and current sum is: 13.
Current sum is: 2.
Left node is: 7. Right node is: 2. Root is: 11.

Root is: 7 and current sum is: 2.
Current sum is: -5.

Root is: 2 and current sum is: 2.
Current sum is: 0.
Has path sum?: True.


Time Complexity: O(n)
Space Complexity: O(log(n))
"""
