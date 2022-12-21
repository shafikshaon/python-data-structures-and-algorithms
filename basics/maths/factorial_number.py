# Factorial number


def main():
    fact = 1

    num = 5
    if num == 0:
        print(f"Factorial of {num} is: {fact}")
    elif num < 0:
        print(f"Factorial is not available for negative number.")
    else:
        for i in range(1, num + 1):
            fact *= i
        print(f"Factorial of {num} is: {fact}")


main()
