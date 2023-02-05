from typing import List


def main(nums1: List[int], nums2: List[int]) -> List[int]:
    print(f"nums1 array: {nums1}, nums2 array: {nums2}.")

    nums1_sort = sorted(nums1)
    nums2_sort = sorted(nums2)

    print(f"After sorting nums1 is {nums1_sort} and nums2 is {nums2_sort}.")

    i, j = 0, 0
    output = []
    while i < len(nums1_sort) and j < len(nums2_sort):
        print(
            f"\nCondition satisfied for [i < len(nums1_sort) and j < len(nums2_sort)] ({i} < {len(nums1_sort)} and {j} < {len(nums2_sort)}) = {i < len(nums1_sort) and j < len(nums2_sort)}."
        )
        if nums1_sort[i] < nums2_sort[j]:
            print(
                f"Currently i = {i}, j = {j}. nums1_sort[i] < nums2_sort[j] ({nums1_sort[i]} < {nums2_sort[j]} = {nums1_sort[i] < nums2_sort[j]}). Incrementing i to {i + 1}."
            )
            i += 1
        elif nums2_sort[j] < nums1_sort[i]:
            print(
                f"Currently i = {i}, j = {j}. nums2_sort[j] < nums1_sort[i] ({nums2_sort[j]} < {nums1_sort[i]} = {nums2_sort[j] < nums1_sort[i]}). Incrementing j to {j + 1}."
            )
            j += 1
        else:
            output.append(nums1_sort[i])
            print(
                "\nCondition: (nums1_sort[i] < nums2_sort[j]) and (nums2_sort[j] < nums1_sort[i]) not satisfied."
            )
            print(
                f"Appending value {nums1_sort[i]} to output array. Now output is {output}."
            )
            print(f"Incrementing i to {i + 1}. Incrementing j to {j + 1}.\n")
            i += 1
            j += 1
    print(f"Final array: {output}.")
    return output


main(nums1=[1, 2, 2, 1], nums2=[2, 2])

# Time complexity - O(nlog(n))
# Space complexity - O(n)
