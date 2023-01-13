def find_sum_of_three(nums, target):
    # Sorting the input list
    nums.sort()

    # Fix one element at a time and find the other two
    for i in range(0, len(nums) - 2):
        # Set the indexes of the two pointers

        # Index of the first of the remaining elements
        low = i + 1

        # Last index
        high = len(nums) - 1

        while low < high:
            # Check if the sum of the triple is equal to the sum
            triple = nums[i] + nums[low] + nums[high]
            # Found a triple whose sum equals the target
            if triple == target:
                return True
                # Move low pointer forward if the triple sum is less
                # than the required sum
            elif triple < target:
                low += 1
                # Move the high pointer backwards if the triple
                # sum is greater than the required sum
            else:
                high -= 1
    return False


def main():
    nums_lists = [
        [3, 7, 1, 2, 8, 4, 5],
        [-1, 2, 1, -4, 5, -3],
        [2, 3, 4, 1, 7, 9],
        [1, -1, 0],
        [2, 4, 2, 7, 6, 3, 1],
    ]

    test_lists = [[10, 20, 21], [-8, 0, 7], [8, 10, 20], [1, -1, 0], [8, 11, 15]]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        for j in range(len(test_lists[i])):
            if find_sum_of_three(nums_lists[i], test_lists[i][j]):
                print("\tSum for", test_lists[i][j], "exists")
            else:
                print("\tSum for", test_lists[i][j], "does not exist")
        print("-" * 100)


if __name__ == "__main__":
    main()

# Time complexity - O(n^2)
# Space' complexity - O(1)
