def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True


# Driver Code
def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("\tThe input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".",
              sep='')
        print("\tIs it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()

# Time complexity - O(n)
# Space' complexity - O(1)
