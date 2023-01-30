# Time Limit Exceed
def main(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    for i in range(n):
        print(f"Current ans: {ans} and x = {x}. ans = {ans * x}.")
        ans = ans * x
    print(f"\nPOW: {ans}.")
    return ans


main(x=2.00000, n=10)

"""
Output:

Current ans: 1 and x = 2.0. ans = 2.0.
Current ans: 2.0 and x = 2.0. ans = 4.0.
Current ans: 4.0 and x = 2.0. ans = 8.0.
Current ans: 8.0 and x = 2.0. ans = 16.0.
Current ans: 16.0 and x = 2.0. ans = 32.0.
Current ans: 32.0 and x = 2.0. ans = 64.0.
Current ans: 64.0 and x = 2.0. ans = 128.0.
Current ans: 128.0 and x = 2.0. ans = 256.0.
Current ans: 256.0 and x = 2.0. ans = 512.0.
Current ans: 512.0 and x = 2.0. ans = 1024.0.

POW: 1024.0.
"""
# Time Complexity: O(n)
# Space Complexity: O(1)
