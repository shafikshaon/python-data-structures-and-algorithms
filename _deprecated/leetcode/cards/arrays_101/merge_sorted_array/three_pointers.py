def main(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1

    for p in range(n + m - 1, -1, -1):
        print(f"Current index: {p}.")
        print(f"p1: {p1} value {nums1[p1]} and p2: {p2} value {nums2[p2]}.")
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        print(f"num1 array is now: {nums1}.\n")
    return nums1


print(main(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))

"""
Output:
Current index: 5.
p1: 2 value 3 and p2: 2 value 6.
num1 array is now: [1, 2, 3, 0, 0, 6].

Current index: 4.
p1: 2 value 3 and p2: 1 value 5.
num1 array is now: [1, 2, 3, 0, 5, 6].

Current index: 3.
p1: 2 value 3 and p2: 0 value 2.
num1 array is now: [1, 2, 3, 3, 5, 6].

Current index: 2.
p1: 1 value 2 and p2: 0 value 2.
num1 array is now: [1, 2, 2, 3, 5, 6].

Current index: 1.
p1: 1 value 2 and p2: -1 value 6.
[1, 2, 2, 3, 5, 6]


Time Complexity: O(n + m)
Space Complexity: O(1)
"""
