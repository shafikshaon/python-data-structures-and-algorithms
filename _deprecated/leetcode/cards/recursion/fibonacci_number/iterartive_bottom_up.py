def main(n):
    if n <= 1:
        return n
    current = 0
    prev1 = 1
    prev2 = 0
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        print(f"Current: {current}. prev1: {prev1}. prev2: {prev2}.")
    return current


print(f"Recursion result: {main(n=10)}.")

"""
Output:
Current: 1. prev1: 1. prev2: 1.
Current: 2. prev1: 2. prev2: 1.
Current: 3. prev1: 3. prev2: 2.
Current: 5. prev1: 5. prev2: 3.
Current: 8. prev1: 8. prev2: 5.
Current: 13. prev1: 13. prev2: 8.
Current: 21. prev1: 21. prev2: 13.
Current: 34. prev1: 34. prev2: 21.
Current: 55. prev1: 55. prev2: 34.
Recursion result: 55.

Time complexity: O(n)
Space complexity: O(1)
"""
