def swapper(i, n, arr):
    for i in reversed(range(i, n - 1)):
        arr[i + 1] = arr[i]


def main(arr):
    n = len(arr)

    i = 0
    while i < n:
        if arr[i] == 0:
            swapper(i, n, arr)
            i += 1
        i += 1
    return arr


print(main(arr=[1, 0, 2, 3, 0, 4, 5, 0]))

"""
Output:
[1, 0, 0, 2, 3, 0, 0, 4]

Time Complexity: O(n)
Space Complexity: O(1)
"""
