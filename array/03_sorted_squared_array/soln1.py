from typing import List


def sorted_squared_array(array: List) -> List:
    expected = []
    for value in array:
        squared_value = value * value
        expected.append(squared_value)
    expected.sort()
    return expected


def main():
    array = [1, 2, 3, 5, 6, 8, 9]
    print(sorted_squared_array(array))


main()

# Time complexity - O(nlog(n))
# Space complexity - O(n)
