def main(n):
    if n <= 1:
        return n
    return main(n - 1) + main(n - 2)


print(f"Recursion result: {main(n=4)}.")

"""
Output:
Recursion result: 3.

Time complexity: O(n)
Space complexity: O(n)
"""
