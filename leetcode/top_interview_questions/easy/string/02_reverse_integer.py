def main(x: int) -> int:
    print(f"Original value: {x}.\n")
    result = 0
    sign = 1

    if x < 0:
        sign = -1
        x = x * sign

    while x > 0:
        print(f"x is now: {x}.")
        remainder = x % 10
        x //= 10
        print(f"Remainder: {remainder}. Quotient: {x}.")
        result = result * 10 + remainder
        print(f"Current reversed value: {result}. and x is: {x}.\n")

    min_val = 2 ** 31 * -1
    max_val = 2 ** 31 - 1
    if result > max_val or result < min_val:
        return 0
    print(f"\nAfter reversing the x is: {result * sign}.")
    return result * sign


main(x=-123)

# Time complexity - O(n)
# Space complexity - O(1)
