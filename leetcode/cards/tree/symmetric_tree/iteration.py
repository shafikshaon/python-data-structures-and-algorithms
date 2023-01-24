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
        l_stack, r_stack = [root], [root]
        while l_stack or r_stack:
            print(
                f"\nLeft stack: {self.print_stack(l_stack)}. Right stack: {self.print_stack(r_stack)}"
            )
            l, r = l_stack.pop(), r_stack.pop()

            if not (l or r):
                continue
            elif not (l and r):
                print(
                    f"The l value: {l.val} and r value: {r.val}. One of the value is missing. So return False."
                )
                return False
            elif l.val != r.val:
                print(
                    f"The l value: {l.val} and r value: {r.val}. Both values are not same. So return False."
                )
                return False

            l_stack.append(l.right)
            l_stack.append(l.left)
            r_stack.append(r.left)
            r_stack.append(r.right)
        return True


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

Left stack: ['1']. Right stack: ['1']

Left stack: ['2', '2']. Right stack: ['2', '2']

Left stack: ['2', '4', '3']. Right stack: ['2', '4', '3']

Left stack: ['2', '4', None, None]. Right stack: ['2', '4', None, None]

Left stack: ['2', '4', None]. Right stack: ['2', '4', None]

Left stack: ['2', '4']. Right stack: ['2', '4']

Left stack: ['2', None, None]. Right stack: ['2', None, None]

Left stack: ['2', None]. Right stack: ['2', None]

Left stack: ['2']. Right stack: ['2']

Left stack: ['3', '4']. Right stack: ['3', '4']

Left stack: ['3', None, None]. Right stack: ['3', None, None]

Left stack: ['3', None]. Right stack: ['3', None]

Left stack: ['3']. Right stack: ['3']

Left stack: [None, None]. Right stack: [None, None]

Left stack: [None]. Right stack: [None]
Is symmetric?: True.



Time Complexity: O(n)
Space Complexity: O(n)
"""
