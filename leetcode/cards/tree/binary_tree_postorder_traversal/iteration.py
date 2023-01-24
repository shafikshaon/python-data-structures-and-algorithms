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

    def post_order_traversal(self, node):
        answer = []
        stack = [node]

        while stack:
            print(f"Current stack is: {self.print_stack(stack)}.")
            current_node = stack[-1]
            if not current_node.left and not current_node.right:
                stack.pop()
                print(
                    f'After pushing "{current_node.val}", stack is: {self.print_stack(stack)}.'
                )
                answer.append(current_node.val)
                print(f"Traversing array is now: {answer}.")

            if current_node.right:
                stack.append(current_node.right)
                current_node.right = None

            if current_node.left:
                stack.append(current_node.left)
                current_node.left = None
            print("\n")
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
print(f"Post order traversal: {tree.post_order_traversal(node=root)}.")

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


Current stack is: ['F', 'G', 'B'].


Current stack is: ['F', 'G', 'B', 'D', 'A'].
After pushing "A", stack is: ['F', 'G', 'B', 'D'].
Traversing array is now: ['A'].


Current stack is: ['F', 'G', 'B', 'D'].


Current stack is: ['F', 'G', 'B', 'D', 'E', 'C'].
After pushing "C", stack is: ['F', 'G', 'B', 'D', 'E'].
Traversing array is now: ['A', 'C'].


Current stack is: ['F', 'G', 'B', 'D', 'E'].
After pushing "E", stack is: ['F', 'G', 'B', 'D'].
Traversing array is now: ['A', 'C', 'E'].


Current stack is: ['F', 'G', 'B', 'D'].
After pushing "D", stack is: ['F', 'G', 'B'].
Traversing array is now: ['A', 'C', 'E', 'D'].


Current stack is: ['F', 'G', 'B'].
After pushing "B", stack is: ['F', 'G'].
Traversing array is now: ['A', 'C', 'E', 'D', 'B'].


Current stack is: ['F', 'G'].


Current stack is: ['F', 'G', 'I'].


Current stack is: ['F', 'G', 'I', 'H'].
After pushing "H", stack is: ['F', 'G', 'I'].
Traversing array is now: ['A', 'C', 'E', 'D', 'B', 'H'].


Current stack is: ['F', 'G', 'I'].
After pushing "I", stack is: ['F', 'G'].
Traversing array is now: ['A', 'C', 'E', 'D', 'B', 'H', 'I'].


Current stack is: ['F', 'G'].
After pushing "G", stack is: ['F'].
Traversing array is now: ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G'].


Current stack is: ['F'].
After pushing "F", stack is: [].
Traversing array is now: ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'].


Post order traversal: ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'].


Time Complexity: O(n)
Space Complexity: O(n)
"""
