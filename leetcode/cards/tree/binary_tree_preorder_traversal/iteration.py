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

    def pre_order_traversal(self, node):
        answer = []
        stack = [node]

        while stack:
            print(f"Current stack is: {self.print_stack(stack)}.")
            current_node = stack.pop()
            if current_node:
                print(f"Current node value: {current_node.val}.\n")
                answer.append(current_node.val)
                stack.append(current_node.right)
                stack.append(current_node.left)
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
print(f"Pre order traversal: {tree.pre_order_traversal(node=root)}.")

"""
Output:

               F
       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
       B               G
   /¯¯¯ ¯¯¯\            ¯¯¯\
   A       D               I
         /¯ ¯\           /¯
         C   E           H
Current stack is: ['F'].
Current node value: F.

Current stack is: ['G', 'B'].
Current node value: B.

Current stack is: ['G', 'D', 'A'].
Current node value: A.

Current stack is: ['G', 'D', None, None].
Current stack is: ['G', 'D', None].
Current stack is: ['G', 'D'].
Current node value: D.

Current stack is: ['G', 'E', 'C'].
Current node value: C.

Current stack is: ['G', 'E', None, None].
Current stack is: ['G', 'E', None].
Current stack is: ['G', 'E'].
Current node value: E.

Current stack is: ['G', None, None].
Current stack is: ['G', None].
Current stack is: ['G'].
Current node value: G.

Current stack is: ['I', None].
Current stack is: ['I'].
Current node value: I.

Current stack is: [None, 'H'].
Current node value: H.

Current stack is: [None, None, None].
Current stack is: [None, None].
Current stack is: [None].
Pre order traversal: ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'].



Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Algorithm
1. Initialize an empty array answer and an empty stack stack.
2. Add root to stack.
3. While stack is not empty, get the top node currNode from stack. If currNode is not NULL:
      i. add its value to answer.
     ii. add its right child to stack.
    iii. add its left child to stack.
    
    Then repeat step 3.
4. Return answer after we empty stack.
"""
