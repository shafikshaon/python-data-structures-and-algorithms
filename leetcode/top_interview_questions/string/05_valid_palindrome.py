def main(s: str) -> bool:
    print(f"Original value of s: {s}.")

    start = 0
    end = len(s) - 1

    while start < end:
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue

        if s[start].lower() != s[end].lower():
            print(f'\n"{s}" is not valid palindrome.')
            return False
        start += 1
        end -= 1
    print(f'\n"{s}" is valid palindrome.')
    return True


main(s="ma dam")
main(s=" ")
main(s="race a car")

# Time complexity - O(n)
# Space complexity - O(1)
