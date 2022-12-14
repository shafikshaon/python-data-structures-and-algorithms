# Swap two numbers

def main():
    a = 5
    b = 6

    a += b
    b -= b
    a -= b

    print(f"a is: {a}, b is: {b}")


main()
