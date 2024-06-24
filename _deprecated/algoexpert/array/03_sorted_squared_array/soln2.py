from typing import List


def sorted_squared_array(array: List) -> List:
    squared_array = [0 for _ in array]
    start_index = 0
    end_index = len(array) - 1

    for idx in reversed(range(len(array))):
        smallest_number = array[start_index]
        largest_number = array[end_index]
        if abs(smallest_number) > abs(largest_number):
            squared_array[idx] = smallest_number * smallest_number
            start_index += 1
        else:
            squared_array[idx] = largest_number * largest_number
            end_index -= 1

    return squared_array


def main():
    array = [1, 2, 3, 5, 6, 8, 9]
    print(sorted_squared_array(array))


main()

# Time complexity - O(n)
# Space complexity - O(n)
