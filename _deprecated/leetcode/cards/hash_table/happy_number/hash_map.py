def squared_calc(n):
    s = 0
    while n > 0:
        temp = n
        n = n // 10
        r = temp % 10
        s += r * r
    print(f"Squared value of {r} is: {r * r} and next value {s + n}.")
    return s


def main(n):
    visited = set()
    while True:
        n = squared_calc(n)
        if n == 1:
            return True
        if n in visited:
            return False
        visited.add(n)


main(n=19)

"""
Output:
Squared value of 1 is: 1 and next value 82.
Squared value of 8 is: 64 and next value 68.
Squared value of 6 is: 36 and next value 100.
Squared value of 1 is: 1 and next value 1.
"""
# Time complexity - O(n)
# Space complexity - O(n)
