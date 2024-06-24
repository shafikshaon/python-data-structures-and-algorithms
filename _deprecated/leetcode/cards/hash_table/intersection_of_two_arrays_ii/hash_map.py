from typing import List


def main(nums1: List[int], nums2: List[int]) -> List[int]:
    print(f"nums1 array: {nums1}, nums2 array: {nums2}.")

    print("Creating an empty dictionary.")
    d = {}

    print(
        f"Loop through the first array ({nums1}) and add the elements and their counts to the dictionary ({d})."
    )
    for num in nums1:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    print(f"d is now {d}.\n")
    result = []

    print(
        f"Loop through the second array ({nums2}) and check if each element exists in the dictionary ({d}).\n"
    )
    for num in nums2:
        if num in d and d[num] > 0:
            print(
                f"Add {num} it to the result array and decrement {d[num]} count in the dictionary."
            )
            result.append(num)
            d[num] -= 1
        else:
            print(f"{num} not found in dictionary {d}. Result array now {result}.")
    print(f"\nFinal array: {result}.")
    return result


main(nums1=[4, 9, 9, 5], nums2=[9, 4, 9, 8, 4])

"""
Output:
nums1 array: [4, 9, 9, 5], nums2 array: [9, 4, 9, 8, 4].
Creating an empty dictionary.
Loop through the first array ([4, 9, 9, 5]) and add the elements and their counts to the dictionary ({}).
d is now {4: 1, 9: 2, 5: 1}.

Loop through the second array ([9, 4, 9, 8, 4]) and check if each element exists in the dictionary ({4: 1, 9: 2, 5: 1}).

Add 9 it to the result array and decrement 2 count in the dictionary.
Add 4 it to the result array and decrement 1 count in the dictionary.
Add 9 it to the result array and decrement 1 count in the dictionary.
8 not found in dictionary {4: 0, 9: 0, 5: 1}. Result array now [9, 4, 9].
4 not found in dictionary {4: 0, 9: 0, 5: 1}. Result array now [9, 4, 9].

Final array: [9, 4, 9].
"""
# Time complexity - O(n)
# Space complexity - O(n)
