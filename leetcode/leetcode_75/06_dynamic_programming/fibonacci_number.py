def main(n: int) -> int:
    print(f"Input number is: {n}.\n")
    if n <= 1:
        return n

    current = 0
    prev1 = 1
    prev2 = 0
    print(f"Current: {current}, prev 1: {prev1}, and prev 2: {prev2}.")
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        print(f"Current: {current}, prev 1: {prev1}, and prev 2: {prev2}.")
    print(f"\nFibonacci number is: {current}.")
    return current


main(n=3)
print(
    "-----------------------------------------------------------------------------------------------------"
)
main(n=4)

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
Input number is: 3.

Current: 0, prev 1: 1, and prev 2: 0.
Current: 1, prev 1: 1, and prev 2: 1.
Current: 2, prev 1: 2, and prev 2: 1.

Fibonacci number is: 2.
-----------------------------------------------------------------------------------------------------
Input number is: 4.

Current: 0, prev 1: 1, and prev 2: 0.
Current: 1, prev 1: 1, and prev 2: 1.
Current: 2, prev 1: 2, and prev 2: 1.
Current: 3, prev 1: 3, and prev 2: 2.

Fibonacci number is: 3.
"""
