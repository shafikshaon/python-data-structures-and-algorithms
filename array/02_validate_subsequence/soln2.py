from typing import List


def validate_subsequence(array: List, sequence: List) -> bool:
    sequence_index = 0
    for value in array:
        if sequence_index == len(sequence):
            break
        if sequence[sequence_index] == value:
            sequence_index += 1
    return sequence_index == len(sequence)


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(validate_subsequence(array, sequence))


main()

# Time complexity - O(n)
# Space complexity - O(1)
