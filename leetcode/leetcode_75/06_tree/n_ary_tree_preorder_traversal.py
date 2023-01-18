class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def print_tree(self):
        if self.children:
            for r in self.children:
                r.print_tree()
        print(self.data)

    def preorder(self):
        _root = self
        if _root is None:
            return []

        stack, output = [
            _root,
        ], []
        while stack:
            _root = stack.pop()
            output.append(int(_root.data))
            print(f"Current output: {output}.")
            stack.extend(reversed(_root.children))

        return output


left = Tree("3")
middle = Tree("2")
right = Tree("4")
root = Tree("1")
root.children = [left, middle, right]
five = Tree("5")
six = Tree("6")
left.children = [five, six]


print(f"Pre order tree: {root.preorder()}")



# Time complexity: O(n)
# Space complexity: O(n)

# Output
"""

"""
