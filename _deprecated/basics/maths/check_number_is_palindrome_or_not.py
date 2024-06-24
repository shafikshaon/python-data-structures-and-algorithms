# Check number is palindrome or not


def main():
    input_number = 121
    temp = input_number
    reversed_number = 0
    while input_number > 0:
        digit = input_number % 10
        reversed_number = reversed_number * 10 + digit
        input_number //= 10
    if temp == reversed_number:
        print(f"{temp} is Palindrome.")
    else:
        print(f"{temp} is not Palindrome.")


main()
