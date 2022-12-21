# Calculate area of triangle


def main():
    a = 5
    b = 6
    c = 7

    s = (a + b + c) / 2  # Calculate semi-perimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print(f"Area is: {area:.2f}")


main()
