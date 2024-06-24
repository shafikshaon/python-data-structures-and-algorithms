# Print prime number in an interval


def main():
    lower_number = 900
    upper_number = 1000
    for num in range(lower_number, upper_number + 1):
        flag = False
        if lower_number > 1:
            for i in range(2, num):
                if num % i == 0:
                    flag = True
                    break
        if not flag:
            print(f"{num} is a prime number")


main()
