from collections import deque


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

    def print_queue(self, queue):
        return [i.val if i else None for i in queue]

    def level_order_traversal(self, root):
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            print(f"Current level: {level}. Currently traversed level: {levels}.")
            levels.append([])

            level_length = len(queue)

            for i in range(level_length):
                print(f"Queue now: {self.print_queue(queue)}.")
                node = queue.popleft()
                print(f"Current value: {node.val} push to level {level}.")
                levels[level].append(node.val)
                if node.left:
                    print(f"Traversing left node: {node.left.val}.\n")
                    queue.append(node.left)
                if node.right:
                    print(f"Traversing right node: {node.right.val}.\n")
                    queue.append(node.right)
            level += 1
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
Current level: 0. Currently traversed level: [].
Queue now: ['F'].
Current value: F push to level 0.
Traversing left node: B.

Traversing right node: G.

Current level: 1. Currently traversed level: [['F']].
Queue now: ['B', 'G'].
Current value: B push to level 1.
Traversing left node: A.

Traversing right node: D.

Queue now: ['G', 'A', 'D'].
Current value: G push to level 1.
Traversing right node: I.

Current level: 2. Currently traversed level: [['F'], ['B', 'G']].
Queue now: ['A', 'D', 'I'].
Current value: A push to level 2.
Queue now: ['D', 'I'].
Current value: D push to level 2.
Traversing left node: C.

Traversing right node: E.

Queue now: ['I', 'C', 'E'].
Current value: I push to level 2.
Traversing left node: H.

Current level: 3. Currently traversed level: [['F'], ['B', 'G'], ['A', 'D', 'I']].
Queue now: ['C', 'E', 'H'].
Current value: C push to level 3.
Queue now: ['E', 'H'].
Current value: E push to level 3.
Queue now: ['H'].
Current value: H push to level 3.
Level order traversal: [['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E', 'H']].


Time Complexity: O(n)
Space Complexity: O(n)
"""
