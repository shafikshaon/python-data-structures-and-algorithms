def main(arr):
    left = 0
    right = len(arr) - 1
    j = 1

    while left < right:
        if arr[left] == arr[j] * 2 or arr[j] == arr[left] * 2:
            return True
        elif j == right:
            left += 1
            j = left + 1
        else:
            j += 1

    return False


print(main(arr=[10, 2, 5, 3]))

"""
Output:
True

Time Complexity: O(n)
Space Complexity: O(1) 
"""
