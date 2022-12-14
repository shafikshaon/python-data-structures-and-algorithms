# Count number of digits in a number


def main():
    input_number = 123456789
    count = 0
    while input_number > 0:
        count += 1
        print(f"Input number: {input_number}.")
        input_number //= 10
        print(f"After Divisor, input_number is: {input_number}")
    print(f"Total number count: {count}")


main()
