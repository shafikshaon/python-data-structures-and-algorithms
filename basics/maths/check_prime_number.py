# Check prime number

def main():
    input_number = 29
    flag = False
    if input_number > 1:
        for i in range(2, input_number):
            if input_number % i == 0:
                flag = True
                break
    if flag:
        print(f"{input_number} is not a prime number")
    else:
        print(f"{input_number} is a prime number")


main()
