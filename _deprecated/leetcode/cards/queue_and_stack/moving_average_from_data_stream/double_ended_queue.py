from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        print(f"Queue  is now: {self.print_queue()}.")
        tail = self.queue.popleft() if self.count > self.size else 0
        print(f"Current window is: {self.print_window(self.count, self.size)}.")
        print(f"Tail is now: {tail}.")
        self.window_sum = self.window_sum - tail + val
        print(f"Window sum is now: {self.window_sum}.")
        print(
            f"Moving average: {self.window_sum / min(self.size, self.count)} ({self.window_sum}/ {min(self.size, self.count)})."
        )
        return self.window_sum / min(self.size, self.count)

    def print_queue(self):
        res = []
        for i in range(len(self.queue)):
            res.append(self.queue[i])
        return res

    def print_window(self, count, size):
        res = []
        for i in range(len(self.queue)):
            if i <= count:
                res.append(self.queue[i])
        return res


obj = MovingAverage(3)
print(f"Size is now: {obj.size}. Window sum: {obj.window_sum}. Count: {obj.count}.")
param_1 = obj.next(1)
print("\n")
param_2 = obj.next(10)
print("\n")
param_3 = obj.next(3)
print("\n")
param_4 = obj.next(5)
print("\n")
param_5 = obj.next(7)
print("\n")
param_6 = obj.next(2)
print("\n")
param_7 = obj.next(8)
print("\n")
param_8 = obj.next(1)
print("\n")
