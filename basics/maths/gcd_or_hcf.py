# GCD or HCF
# HCF (Highest Common Factor) is also known as Greatest Common Divisor (GCD)


def main():
    first = 12
    second = 18

    gcd = 1
    for i in range(1, first + 1):
        if first % i == 0 and second % i == 0:
            gcd = i
    print("HCF or GCD of %d and %d is %d" % (first, second, gcd))

    lcm = first * second / gcd
    print("LCM of %d and %d is %d" % (first, second, lcm))


main()
