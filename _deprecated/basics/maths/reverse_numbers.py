# Reverse numbers


def main():
    input_number = 123456789
    reversed_number = 0
    while input_number > 0:
        digit = input_number % 10
        print(f"Divisor: {digit}")
        reversed_number = reversed_number * 10 + digit
        print(f"Reversed number: {reversed_number}")
        input_number //= 10


main()
