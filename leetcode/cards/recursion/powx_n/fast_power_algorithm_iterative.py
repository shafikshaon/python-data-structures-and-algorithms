# Time Limit Exceed
def main(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    current_product = x
    while n > 0:
        print(
            f"Current ans: {ans} and n = {n}. ans = {ans}. Current product: {current_product}."
        )
        if n % 2 == 1:
            ans *= current_product
        current_product *= current_product
        n = n // 2
    print(f"\nPOW: {ans}.")
    return ans


main(x=2.00000, n=10)
# main(x=0.00001, n=2147483647)
"""
Output:
Current ans: 1 and n = 10. ans = 1. Current product: 2.0.
Current ans: 1 and n = 5. ans = 1. Current product: 4.0.
Current ans: 4.0 and n = 2. ans = 4.0. Current product: 16.0.
Current ans: 4.0 and n = 1. ans = 4.0. Current product: 256.0.

POW: 1024.0.

"""
# Time Complexity: O(logn)
# Space Complexity: O(1)
