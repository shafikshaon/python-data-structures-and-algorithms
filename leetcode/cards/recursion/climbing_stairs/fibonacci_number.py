def main(n):
    if n == 1:
        return n
    prev1 = 1
    prev2 = 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev1
        prev2 = current
    return prev2


print(f"Distinct ways: {main(n=3)}.")

"""
Output:
Distinct ways: 3.

Time complexity: O(n)
Space complexity: O(1)
"""
