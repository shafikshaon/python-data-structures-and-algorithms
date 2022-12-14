# Find the sum of natural number

def main():
    num = 16
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(f"Sum: {sum}")


main()
