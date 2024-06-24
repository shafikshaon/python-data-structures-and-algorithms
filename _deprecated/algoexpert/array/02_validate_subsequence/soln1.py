from typing import List


def validate_subsequence(array: List, sequence: List) -> bool:
    array_index = sequence_index = 0
    while len(array) > array_index and len(sequence) > sequence_index:
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(validate_subsequence(array, sequence))


main()

# Time complexity - O(n)
# Space complexity - O(1)
