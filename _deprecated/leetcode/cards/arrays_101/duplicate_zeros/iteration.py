def main(arr):
    output = []
    for i in arr:
        if i == 0:
            output.append(0)
            output.append(0)
        else:
            output.append(i)
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr


print(main(arr=[1, 0, 2, 3, 0, 4, 5, 0]))

"""
Output:
[1, 0, 0, 2, 3, 0, 0, 4]

Time Complexity: O(n)
Space Complexity: O(n)
"""
