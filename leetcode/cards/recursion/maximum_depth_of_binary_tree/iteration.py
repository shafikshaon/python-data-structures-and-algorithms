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
        return [i[1].val if i and i[1] else None for i in stack]

    def max_depth(self, root):
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            if len(stack):
                print(f"\nStack is now: {self.print_stack(stack)}.")
            current_depth, root = stack.pop()
            if root:
                print(
                    f"Current depth is: {current_depth}. Current node is: {root.val if root else None}."
                )
            if root:
                depth = max(depth, current_depth)
                print(f"Max depth till now: {depth}.")
                if root.left:
                    print(f"Adding left node: {root.left.val} in the stack.")
                stack.append((current_depth + 1, root.left))
                if root.right:
                    print(f"Adding right node: {root.right.val} in the stack.")
                stack.append((current_depth + 1, root.right))
        return depth


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

Stack is now: ['3'].
Current depth is: 1. Current node is: 3.
Max depth till now: 1.
Adding left node: 9 in the stack.
Adding right node: 20 in the stack.

Stack is now: ['9', '20'].
Current depth is: 2. Current node is: 20.
Max depth till now: 2.
Adding left node: 15 in the stack.
Adding right node: 7 in the stack.

Stack is now: ['9', '15', '7'].
Current depth is: 3. Current node is: 7.
Max depth till now: 3.

Stack is now: ['9', '15', None, None].

Stack is now: ['9', '15', None].

Stack is now: ['9', '15'].
Current depth is: 3. Current node is: 15.
Max depth till now: 3.

Stack is now: ['9', None, None].

Stack is now: ['9', None].

Stack is now: ['9'].
Current depth is: 2. Current node is: 9.
Max depth till now: 3.

Stack is now: [None, None].

Stack is now: [None].
Max depth: 3.




Time Complexity: O(n)
Space Complexity: O(log(n))
In the worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log(N)). Therefore, the space complexity in this case would be O(log(N).
"""
