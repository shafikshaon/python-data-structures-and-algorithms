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

    def in_order_traversal(self, node):
        answer = []
        curr = root

        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree.
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right  # move to next right node
            else:
                # has a left subtree
                last = curr.left
                while last.right:  # find rightmost
                    last = last.right
                last.right = curr  # put cur after the pre node
                temp = curr  # store cur node
                curr = curr.left  # move cur to the top of the new tree
                temp.left = None  # original cur left be null, avoid infinite loops
        return answer


root = TreeNode("F")
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
g = TreeNode("G")
h = TreeNode("H")
i = TreeNode("I")

root.left = b
root.right = g
root.left.left = a
root.left.right = d
root.left.right.left = c
root.left.right.right = e
root.right.right = i
root.right.right.left = h

root.print_tree()

tree = TreeNode()
print(f"In order traversal: {tree.in_order_traversal(node=root)}.")

"""
Output:
               F
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       B               G
   /¯¯¯ ¯¯¯\            ¯¯¯\
   A       D               I
         /¯ ¯\           /¯
         C   E           H
In order traversal: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'].


Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
Algorithm
1. Initialize current as root
2. While curr is not NULL, check if it doesn't has a left child:
      i. Add current’s value
     ii. Go to the right, i.e., current = current.right
3. else:
      i. In current's left subtree, make current the right child of the rightmost node
     ii. Go to this left child, i.e., current = current.left
"""
