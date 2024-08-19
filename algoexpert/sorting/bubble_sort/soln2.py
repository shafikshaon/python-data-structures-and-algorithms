def bubble_sort(array):
    is_sorted = False
    counter = 0

    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter += 1
    return array


print(bubble_sort([5, 4, 3, 2, 1]))

# Best case
# Time complexity: O(n)
# Space complexity: O(1)

# Average case
# Time complexity: O(n^2)
# Space complexity: O(1)

# Worst case
# Time complexity: O(n^2)
# Space complexity: O(1)
