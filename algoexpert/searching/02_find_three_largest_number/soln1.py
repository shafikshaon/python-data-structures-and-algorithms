# Question tag:  Easy

"""
Problem Statement:
- Given array of at least three integers
- Return the largest three integers
- You can't sort the array

Sample Input:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output:
[18, 141, 541]
"""
from typing import List


def shift_number_n_update(output_array, idx, val):
    for i in range(idx + 1):
        if i == idx:
            output_array[i] = val
        else:
            output_array[i] = output_array[i + 1]


def main(array: List) -> List:
    print(f"Input array: {array}.")
    output_array = [None, None, None]
    for i in range(len(array)):
        val = array[i]
        print(f"Current value: {val}. Output array is now: {output_array}.")
        if output_array[2] is None or val > output_array[2]:
            shift_number_n_update(output_array, 2, val)
        elif output_array[1] is None or val > output_array[1]:
            shift_number_n_update(output_array, 1, val)
        elif output_array[0] is None or val > output_array[0]:
            shift_number_n_update(output_array, 0, val)
    print(f"Output array: {output_array}.\n\n")
    return output_array


if __name__ == "__main__":
    main(array=[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7])
    main(array=[55, 7, 8])
    main(array=[55, 43, 11, 3, -3, 10])
    main(array=[7, 8, 3, 11, 43, 55])

"""
Output:
Input array: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7].
Current value: 141. Output array is now: [None, None, None].
Current value: 1. Output array is now: [None, None, 141].
Current value: 17. Output array is now: [None, 1, 141].
Current value: -7. Output array is now: [1, 17, 141].
Current value: -17. Output array is now: [1, 17, 141].
Current value: -27. Output array is now: [1, 17, 141].
Current value: 18. Output array is now: [1, 17, 141].
Current value: 541. Output array is now: [17, 18, 141].
Current value: 8. Output array is now: [18, 141, 541].
Current value: 7. Output array is now: [18, 141, 541].
Current value: 7. Output array is now: [18, 141, 541].
Output array: [18, 141, 541].


Input array: [55, 7, 8].
Current value: 55. Output array is now: [None, None, None].
Current value: 7. Output array is now: [None, None, 55].
Current value: 8. Output array is now: [None, 7, 55].
Output array: [7, 8, 55].


Input array: [55, 43, 11, 3, -3, 10].
Current value: 55. Output array is now: [None, None, None].
Current value: 43. Output array is now: [None, None, 55].
Current value: 11. Output array is now: [None, 43, 55].
Current value: 3. Output array is now: [11, 43, 55].
Current value: -3. Output array is now: [11, 43, 55].
Current value: 10. Output array is now: [11, 43, 55].
Output array: [11, 43, 55].


Input array: [7, 8, 3, 11, 43, 55].
Current value: 7. Output array is now: [None, None, None].
Current value: 8. Output array is now: [None, None, 7].
Current value: 3. Output array is now: [None, 7, 8].
Current value: 11. Output array is now: [3, 7, 8].
Current value: 43. Output array is now: [7, 8, 11].
Current value: 55. Output array is now: [8, 11, 43].
Output array: [11, 43, 55].


"""

"""
Time complexity: O(n)
Space complexity: O(1)
"""
