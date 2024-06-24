class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        print(f"\nAdd {x} in the queue.")
        self.s1.append(x)
        print(f"s1 is now: {self.s1}.")

    def pop(self) -> int:
        print(f"s2 is before pop: {self.s2}.")
        self.peek()
        _popped_value = self.s2.pop()
        print(f"s2 is after pop: {self.s2}.")
        return _popped_value

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        print(f"Peek value: {self.s2[-1]}.")
        return self.s2[-1]

    def empty(self) -> bool:
        print(f"Is queue is empty: {not self.s1 and not self.s2}.")
        return not self.s1 and not self.s2


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
s1 is now: [1].

Add 2 in the queue.
s1 is now: [1, 2].

Add 3 in the queue.
s1 is now: [1, 2, 3].

Add 4 in the queue.
s1 is now: [1, 2, 3, 4].

Add 5 in the queue.
s1 is now: [1, 2, 3, 4, 5].

Add 6 in the queue.
s1 is now: [1, 2, 3, 4, 5, 6].


s2 is before pop: [].
Peek value: 1.
s2 is after pop: [6, 5, 4, 3, 2].


Peek value: 2.


Is queue is empty: False.
"""

"""
Push:
Time complexity: O(1)
Space complexity: O(n)

Pop:
Time complexity: Amortized O(1), Worst-case O(n).
Space complexity: O(1)

Peek:
Time complexity: O(1)
Space complexity: O(1)

Empty:
Time complexity: O(1)
Space complexity: O(1)
"""
