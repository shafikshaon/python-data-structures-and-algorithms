from typing import List


def main(digits: List[int]) -> List:
    print(f"Original array: {digits}\n")
    n: int = len(digits)
    for i in range(n):
        idx = n - 1 - i
        print(f"Current index is: {idx} and value is: {digits[idx]}.")
        if digits[idx] == 9:
            digits[idx] = 0
            print(f"Found 9 at index {idx}, set 0.")
        else:
            print(
                f"Current index is: {idx}, value is: {digits[idx]}  and value incremented to: {digits[idx] + 1}."
            )
            digits[idx] += 1
            print(f"Final list will be {digits}")
            return digits
    print(f"Append 1 to the list and list will be {[1] + digits}")
    return [1] + digits


main(digits=[2, 1, 9])
print("\n----------------------------------------------------\n")
main(digits=[9, 9])

# Time complexity - O(n)
# Space complexity - O(n)
