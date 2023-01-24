def main(num: int) -> str:
    suffix = "th"
    if num == 0:
        suffix = ""
    if num % 10 == 1 and num % 100 != 11:
        suffix = "st"
    if num % 10 == 2 and num % 100 != 12:
        suffix = "nd"
    if num % 10 == 3 and num % 100 != 13:
        suffix = "rd"

    return str(num) + suffix


print(main(1))
print(main(2))
print(main(3))
print(main(4))
print(main(11))
print(main(13))
print(main(21))
print(main(51))
print(main(52))
print(main(53))
print(main(54))
