class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        print(f"Stack is now: {self.stack} and min stack is: {self.min_stack}.")
        print(f"Push {val} to stack.")
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            print(
                f"Value: {val}. Min stack last value is: {self.min_stack[-1] if self.min_stack else None}."
            )
            self.min_stack.append(val)
        print(
            f"After push. Stack is now: {self.stack} and min stack is: {self.min_stack}."
        )

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            print(f"Pop {self.min_stack[-1]} from min stack.")
            self.min_stack.pop()
        print(f"Pop {self.stack[-1]} from stack.")
        self.stack.pop()

    def top(self) -> int:
        print(f"Stack top: {self.stack[-1]}.")
        return self.stack[-1]

    def getMin(self) -> int:
        print(f"Min stack top: {self.min_stack[-1]}.")
        return self.min_stack[-1]


obj = MinStack()
obj.push(1)
print("\n")
obj.push(2)
print("\n")
obj.push(3)
print("\n")
obj.push(4)
print("\n")
obj.push(5)
print("\n")
obj.push(6)
print("\n")
obj.push(7)
print("\n")
obj.push(8)
print("\n")
obj.push(9)
print("\n")
obj.pop()
print(
    "\n---------------------------------------------------------------------------------------\n"
)
obj.top()
obj.getMin()

"""
Output:
Stack is now: [] and min stack is: [].
Push 1 to stack.
Value: 1. Min stack last value is: None.
After push. Stack is now: [1] and min stack is: [1].


Stack is now: [1] and min stack is: [1].
Push 2 to stack.
After push. Stack is now: [1, 2] and min stack is: [1].


Stack is now: [1, 2] and min stack is: [1].
Push 3 to stack.
After push. Stack is now: [1, 2, 3] and min stack is: [1].


Stack is now: [1, 2, 3] and min stack is: [1].
Push 4 to stack.
After push. Stack is now: [1, 2, 3, 4] and min stack is: [1].


Stack is now: [1, 2, 3, 4] and min stack is: [1].
Push 5 to stack.
After push. Stack is now: [1, 2, 3, 4, 5] and min stack is: [1].


Stack is now: [1, 2, 3, 4, 5] and min stack is: [1].
Push 6 to stack.
After push. Stack is now: [1, 2, 3, 4, 5, 6] and min stack is: [1].


Stack is now: [1, 2, 3, 4, 5, 6] and min stack is: [1].
Push 7 to stack.
After push. Stack is now: [1, 2, 3, 4, 5, 6, 7] and min stack is: [1].


Stack is now: [1, 2, 3, 4, 5, 6, 7] and min stack is: [1].
Push 8 to stack.
After push. Stack is now: [1, 2, 3, 4, 5, 6, 7, 8] and min stack is: [1].


Stack is now: [1, 2, 3, 4, 5, 6, 7, 8] and min stack is: [1].
Push 9 to stack.
After push. Stack is now: [1, 2, 3, 4, 5, 6, 7, 8, 9] and min stack is: [1].


Pop 9 from stack.

---------------------------------------------------------------------------------------

Stack top: 8.
Min stack top: 1.


Time Complexity: O(1)
Space complexity: O(n)
"""
