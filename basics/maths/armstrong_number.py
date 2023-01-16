# Armstrong number
# A positive integer is called an Armstrong number of order n if

# abcd... = an + bn + cn + dn + ...
# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


def main():
    input_number = 153
    temp = input_number
    sum = 0
    while input_number > 0:
        digit = input_number % 10
        sum = sum + digit**3
        input_number //= 10

    if sum == temp:
        print(f"{temp} is a armstrong number")
    else:
        print(f"{temp} is not a armstrong number")


main()
