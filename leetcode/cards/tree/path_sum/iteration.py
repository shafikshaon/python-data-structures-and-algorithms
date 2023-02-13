class TreeNode:
    answer = []

    def __init__(self, val=0, left=None, right=None):
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
        stack = [(root, sum - root.val)]
        while stack:
            print(f"\nCurrent stack is: {self.print_stack(stack)}.")
            node, curr_sum = stack.pop()
            print(
                f"Current node value: {node.val if node else None}. Current sum: {curr_sum}."
            )
            if not node.left and not node.right and curr_sum == 0:
                print(
                    f"Left is: {node.left}, Right is: {node.right}, and Current sum: {curr_sum}. So, return True."
                )
                return True
            if node.right:
                print(
                    f"Right node is: {node.right.val} and it's root is: {node.val}. Pushing {node.right.val} to stack."
                )
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                print(
                    f"Left node is: {node.left.val} and it's root is: {node.val}. Pushing {node.left.val} to stack."
                )
                stack.append((node.left, curr_sum - node.left.val))
        return False


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

Current stack is: [5].
Current node value: 5. Current sum: 17.
Right node is: 8 and it's root is: 5. Pushing 8 to stack.
Left node is: 4 and it's root is: 5. Pushing 4 to stack.

Current stack is: [8, 4].
Current node value: 4. Current sum: 13.
Left node is: 11 and it's root is: 4. Pushing 11 to stack.

Current stack is: [8, 11].
Current node value: 11. Current sum: 2.
Right node is: 2 and it's root is: 11. Pushing 2 to stack.
Left node is: 7 and it's root is: 11. Pushing 7 to stack.

Current stack is: [8, 2, 7].
Current node value: 7. Current sum: -5.

Current stack is: [8, 2].
Current node value: 2. Current sum: 0.
Left is: None, Right is: None, and Current sum: 0. So, return True.
Has path sum?: True.

Time Complexity: O(n)
Space Complexity: O(log(n))
"""
