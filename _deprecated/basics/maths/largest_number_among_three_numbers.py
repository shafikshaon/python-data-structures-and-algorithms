# Find the largest number among three number


def main():
    a = 10
    b = 14
    c = 12

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    print(f"Largest number is: {largest}")


main()
