class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            print(f"Queue is full. So {value} can't enqueue.")
            return False
        print(f"Enqueue {value} in queue.")
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        print(f"Count is: {self.count}. Queue is now: {self.print_queue()}")
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            print(
                f"Total element is queue is: {self.count}. So, dequeue is not possible."
            )
            return False
        self.head = self.head.next
        self.count -= 1
        print(
            f"Dequeue from queue. Count is: {self.count} and queue is now: {self.print_queue()}."
        )
        return True

    def Front(self) -> int:
        if self.count == 0:
            print(f"Queue element count: {self.count} so there is no front element.")
            return -1
        print(f"Front element is: {self.head.value}.")
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:
            print(f"Queue element count: {self.count} so there is no front element.")
            return -1
        print(
            f"Rear element is: {self.tail.value}."
        )
        return self.tail.value

    def isEmpty(self) -> bool:
        print(f"Queue element count: {self.count}. Is queue empty? {self.count == 0}.")
        return self.count == 0

    def isFull(self) -> bool:
        print(f"Queue capacity: {self.capacity}. Queue element count: {self.count}.")
        return self.count == self.capacity

    def print_queue(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


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
Enqueue 1 in queue.
Count is: 1. Queue is now: [1]
Enqueue 2 in queue.
Count is: 2. Queue is now: [1, 2]
Enqueue 3 in queue.
Count is: 3. Queue is now: [1, 2, 3]
Enqueue 4 in queue.
Count is: 4. Queue is now: [1, 2, 3, 4]
Enqueue 5 in queue.
Count is: 5. Queue is now: [1, 2, 3, 4, 5]
Enqueue 6 in queue.
Count is: 6. Queue is now: [1, 2, 3, 4, 5, 6]
Enqueue 7 in queue.
Count is: 7. Queue is now: [1, 2, 3, 4, 5, 6, 7]
Enqueue 8 in queue.
Count is: 8. Queue is now: [1, 2, 3, 4, 5, 6, 7, 8]
Enqueue 9 in queue.
Count is: 9. Queue is now: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Queue is full. So 10 can't enqueue.
Dequeue from queue. Count is: 8 and queue is now: [2, 3, 4, 5, 6, 7, 8, 9].
Front element is: 2.
Rear element is: 9.
Queue element count: 8. Is queue empty? False.
Queue capacity: 9. Queue element count: 8.


Time complexity: O(1)
Space complexity: O(n)
"""
