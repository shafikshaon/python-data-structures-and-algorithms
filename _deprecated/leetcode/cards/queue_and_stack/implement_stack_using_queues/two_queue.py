from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        print(f"\nPushing {x} in stack.")
        print(f"q2 is: {self.q2} and q1 is: {self.q1}.")
        self.q2.clear()
        self.q1.append(x)
        for i in range(len(self.q1) - 1, -1, -1):
            self.q2.append(self.q1[i])
        print(f"q2 now: {self.q2}.")

    def pop(self) -> int:
        print(f"Before popping, q2 is {self.q2}.")
        num = self.q2.popleft()
        self.q1.clear()
        for i in range(len(self.q2) - 1, -1, -1):
            self.q1.append(self.q2[i])
        print(f"{num} popped.")
        print(f"After popping, q2 is {self.q2}.")
        return num

    def top(self) -> int:
        print(f"Top is: {self.q2[0]}.")
        return self.q2[0]

    def empty(self) -> bool:
        if len(self.q1) == 0:
            print(f"Is stack empty? True.")
            return True
        else:
            print(f"Is stack empty? False.")
            return False


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

"""
Output:
Pushing 1 in stack.
q2 is: deque([]) and q1 is: deque([]).
q2 now: deque([1]).

Pushing 2 in stack.
q2 is: deque([1]) and q1 is: deque([1]).
q2 now: deque([2, 1]).

Pushing 3 in stack.
q2 is: deque([2, 1]) and q1 is: deque([1, 2]).
q2 now: deque([3, 2, 1]).

Pushing 4 in stack.
q2 is: deque([3, 2, 1]) and q1 is: deque([1, 2, 3]).
q2 now: deque([4, 3, 2, 1]).

Pushing 5 in stack.
q2 is: deque([4, 3, 2, 1]) and q1 is: deque([1, 2, 3, 4]).
q2 now: deque([5, 4, 3, 2, 1]).
Before popping, q2 is deque([5, 4, 3, 2, 1]).
5 popped.
After popping, q2 is deque([4, 3, 2, 1]).
Top is: 4.
Is stack empty? False.

"""

"""
Push:
Time complexity: O(n)
Space complexity: O(n)

Pop:
Time complexity: O(n)
Space complexity: O(n)

Peek:
Time complexity: O(1)
Space complexity: O(1)

Empty:
Time complexity: O(1)
Space complexity: O(1)
"""
