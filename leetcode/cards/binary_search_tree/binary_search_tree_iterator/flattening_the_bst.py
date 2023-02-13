# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.nodes_sorted)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def print_tree(self, root):
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


# Use the insert method to add nodes
root = TreeNode(6)
left = TreeNode(4)
right = TreeNode(10)
root.left = left
root.right = right

root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(12)

# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
obj.print_tree(root=root)

inputs = [
    "BSTIterator",
    "next",
    "next",
    "hasNext",
    "next",
    "hasNext",
    "next",
    "hasNext",
    "next",
    "hasNext",
]
for i in inputs:
    if i == "next":
        print(f"next: {obj.next()}.")
    elif i == "hasNext":
        print(f"has next: {obj.hasNext()}.")

# Time complexity: O(n)
# Space complexity: O(n)
