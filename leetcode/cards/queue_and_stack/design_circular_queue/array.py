class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.head_index = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            print(f"Queue is full. So {value} can't enqueue.")
            return False
        self.queue[(self.head_index + self.count) % self.capacity] = value
        print(
            f"Enqueue {value} at index {(self.head_index + self.count) % self.capacity}. Now queue is: {self.queue}."
        )
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            print(
                f"Total element is queue is: {self.count}. So, dequeue is not possible."
            )
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        print(
            f"Dequeue from queue. Head index now: {self.head_index} and count is: {self.count}. Now queue is: {self.queue}."
        )
        return True

    def Front(self) -> int:
        if self.count == 0:
            print(f"Queue element count: {self.count} so there is no front element.")
            return -1
        print(f"Front element is: {self.queue[self.head_index]}.")
        return self.queue[self.head_index]

    def Rear(self) -> int:
        if self.count == 0:
            print(f"Queue element count: {self.count} so there is no front element.")
            return -1
        print(
            f"Front element is: {self.queue[(self.head_index + self.count - 1) % self.capacity]}."
        )
        return self.queue[(self.head_index + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        print(f"Queue element count: {self.count}. Is queue empty? {self.count == 0}.")
        return self.count == 0

    def isFull(self) -> bool:
        print(f"Queue capacity: {self.capacity}. Queue element count: {self.count}.")
        return self.count == self.capacity


obj = MyCircularQueue(9)
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in input:
    param_1 = obj.enQueue(i)
param_2 = obj.deQueue()

param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()

"""
Output:
Enqueue 1 at index 0. Now queue is: [1, 0, 0, 0, 0, 0, 0, 0, 0].
Enqueue 2 at index 1. Now queue is: [1, 2, 0, 0, 0, 0, 0, 0, 0].
Enqueue 3 at index 2. Now queue is: [1, 2, 3, 0, 0, 0, 0, 0, 0].
Enqueue 4 at index 3. Now queue is: [1, 2, 3, 4, 0, 0, 0, 0, 0].
Enqueue 5 at index 4. Now queue is: [1, 2, 3, 4, 5, 0, 0, 0, 0].
Enqueue 6 at index 5. Now queue is: [1, 2, 3, 4, 5, 6, 0, 0, 0].
Enqueue 7 at index 6. Now queue is: [1, 2, 3, 4, 5, 6, 7, 0, 0].
Enqueue 8 at index 7. Now queue is: [1, 2, 3, 4, 5, 6, 7, 8, 0].
Enqueue 9 at index 8. Now queue is: [1, 2, 3, 4, 5, 6, 7, 8, 9].
Queue is full. So 10 can't enqueue.
Dequeue from queue. Head index now: 1 and count is: 8. Now queue is: [1, 2, 3, 4, 5, 6, 7, 8, 9].
Front element is: 2.
Front element is: 9.
Queue element count: 8. Is queue empty? False.
Queue capacity: 9. Queue element count: 8.


Time complexity: O(1)
Space complexity: O(n)
"""
