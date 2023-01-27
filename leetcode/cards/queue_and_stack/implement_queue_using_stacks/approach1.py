class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        print(f"\nAdd {x} in the queue.")
        while self.s1:
            self.s2.append(self.s1.pop())
        print(f"s2 is now: {self.s2}.")
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        print(f"s1 is now: {self.s1}.")

    def pop(self) -> int:
        print(f"s1 is before pop: {self.s1}.")
        _popped_value = self.s1.pop()
        print(f"s1 is after pop: {self.s1}.")
        return _popped_value

    def peek(self) -> int:
        print(f"Peek value: {self.s1[-1]}.")
        return self.s1[-1]

    def empty(self) -> bool:
        print(f"Is queue is empty: {not self.s1}.")
        return not self.s1


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
print("\n")
param_2 = obj.pop()
print("\n")
param_3 = obj.peek()
print("\n")
param_4 = obj.empty()

"""
Output:
Add 1 in the queue.
s2 is now: [].
s1 is now: [1].

Add 2 in the queue.
s2 is now: [1].
s1 is now: [2, 1].

Add 3 in the queue.
s2 is now: [1, 2].
s1 is now: [3, 2, 1].

Add 4 in the queue.
s2 is now: [1, 2, 3].
s1 is now: [4, 3, 2, 1].

Add 5 in the queue.
s2 is now: [1, 2, 3, 4].
s1 is now: [5, 4, 3, 2, 1].

Add 6 in the queue.
s2 is now: [1, 2, 3, 4, 5].
s1 is now: [6, 5, 4, 3, 2, 1].


s1 is before pop: [6, 5, 4, 3, 2, 1].
s1 is after pop: [6, 5, 4, 3, 2].


Peek value: 2.


Is queue is empty: False.
"""

"""
Push:
Time complexity: O(n)
Space complexity: O(n)

Pop:
Time complexity: O(1)
Space complexity: O(1)

Peek:
Time complexity: O(1)
Space complexity: O(1)

Empty:
Time complexity: O(1)
Space complexity: O(1)
"""
