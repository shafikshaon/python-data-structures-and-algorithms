# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if root.val > val else root.right
        return root

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


# root = [4,2,7,1,3], val = 2
# Use the insert method to add nodes
root = TreeNode(4)
left = TreeNode(2)
right = TreeNode(7)
root.left = left
root.right = right

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Your BSTIterator object will be instantiated and called as such:
obj = Solution()
obj.print_tree(root=root)

_search = obj.searchBST(root, 2)
print(f"Search 2: {_search.val if _search else None}")

# Time complexity: O(h), h is height of the tree
# Space complexity: O(1)

"""
Output:
       4
   /¯¯¯ ¯¯¯\
   2       7
 /¯ ¯\
 1   3
Search 2: 2
"""
