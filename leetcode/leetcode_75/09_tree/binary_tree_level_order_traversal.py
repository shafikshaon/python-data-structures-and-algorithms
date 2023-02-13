from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
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
                valstr = str(n[0].data)
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

    def level_order(self):
        levels_output = []

        if not root:
            return levels_output

        level = 0
        queue = deque(
            [
                root,
            ]
        )

        queue_for_print = []

        while queue:
            # start the current level
            levels_output.append([])
            # number of elements in the current levels
            level_length = len(queue)
            print(f"Current level is: {level} and levels length is: {level_length}.")

            # iterate over child elements
            for i in range(level_length):
                node = queue.popleft()
                queue_for_print.append(node.data)
                # fulfill the current level
                levels_output[level].append(node.data)

                # add child nodes of the current level in the queue for the next level
                if node.left:
                    queue_for_print.append(node.left.data)
                    queue.append(node.left)
                if node.right:
                    queue_for_print.append(node.right.data)
                    queue.append(node.right)
            print(f"Current queue: {queue_for_print}.")
            print(f"Current level traverse: {levels_output}.\n")
            queue_for_print = []
            level += 1
        return levels_output


# Use the insert method to add nodes
root = Node(3)
left = Node(9)
right = Node(20)
root.left = left
root.right = right

fifteen = Node(15)
seven = Node(7)
root.right.left = fifteen
root.right.right = seven
root.print_tree()

print(f"Level order tree: {root.level_order()}")

# Input: root = [3,9,20,null,null,15,7]
# Time complexity: O(n)
# Space complexity: O(n)

# Output
"""
9
3
15
20
7
Current level is: 0 and levels length is: 1.
Current queue: [3, 9, 20].
Current level traverse: [[3]].

Current level is: 1 and levels length is: 2.
Current queue: [9, 20, 15, 7].
Current level traverse: [[3], [9, 20]].

Current level is: 2 and levels length is: 2.
Current queue: [15, 7].
Current level traverse: [[3], [9, 20], [15, 7]].

Level order tree: [[3], [9, 20], [15, 7]]
"""
