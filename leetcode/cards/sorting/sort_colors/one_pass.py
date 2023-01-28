def main(nums):
    print(f"Input: {nums}.")
    print("0 => Red, 1=> White, 2=> Blue.\n")
    p0 = curr = 0
    p2 = len(nums) - 1

    while curr <= p2:
        print(f"Color before swapping: {nums}.")
        print(f"p0 => {p0}, curr => {curr}, p2 => {p2}.")
        print(f"Current color is: {nums[curr]}.")
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1

        print(f"Color after  swapping: {nums}.")
        print(f"p0 => {p0}, curr => {curr}, p2 => {p2}.\n")
    print(f"\nOutput: {nums}.")


main(nums=[2, 0, 2, 1, 1, 0])

"""
Output:
Input: [2, 0, 2, 1, 1, 0].
0 => Red, 1=> White, 2=> Blue.

Color before swapping: [2, 0, 2, 1, 1, 0].
p0 => 0, curr => 0, p2 => 5.
Current color is: 2.
Color after  swapping: [0, 0, 2, 1, 1, 2].
p0 => 0, curr => 0, p2 => 4.

Color before swapping: [0, 0, 2, 1, 1, 2].
p0 => 0, curr => 0, p2 => 4.
Current color is: 0.
Color after  swapping: [0, 0, 2, 1, 1, 2].
p0 => 1, curr => 1, p2 => 4.

Color before swapping: [0, 0, 2, 1, 1, 2].
p0 => 1, curr => 1, p2 => 4.
Current color is: 0.
Color after  swapping: [0, 0, 2, 1, 1, 2].
p0 => 2, curr => 2, p2 => 4.

Color before swapping: [0, 0, 2, 1, 1, 2].
p0 => 2, curr => 2, p2 => 4.
Current color is: 2.
Color after  swapping: [0, 0, 1, 1, 2, 2].
p0 => 2, curr => 2, p2 => 3.

Color before swapping: [0, 0, 1, 1, 2, 2].
p0 => 2, curr => 2, p2 => 3.
Current color is: 1.
Color after  swapping: [0, 0, 1, 1, 2, 2].
p0 => 2, curr => 3, p2 => 3.

Color before swapping: [0, 0, 1, 1, 2, 2].
p0 => 2, curr => 3, p2 => 3.
Current color is: 1.
Color after  swapping: [0, 0, 1, 1, 2, 2].
p0 => 2, curr => 4, p2 => 3.


Output: [0, 0, 1, 1, 2, 2].


Time complexity: O(n)
Space complexity: O(1)
"""
