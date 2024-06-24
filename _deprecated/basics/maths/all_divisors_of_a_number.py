# All divisors of a number


def main():
    input_number = 20

    for i in range(1, input_number + 1):
        if input_number % i == 0:
            print(f"{i}")


main()
