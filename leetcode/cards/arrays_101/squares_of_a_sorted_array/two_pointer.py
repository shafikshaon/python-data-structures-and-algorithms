def main(nums):
    n = len(nums)
    output = [0] * n
    left = 0
    right = n - 1

    print(f"Input array: {nums}.\n")

    for i in range(n - 1, -1, -1):
        print(
            f"Current index is: {i}. Comparing left and right index value. Left index {left} and right index {right}. {abs(nums[left])} < {abs(nums[right])}."
        )
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        print(f"Current square is: {square * square}.")
        output[i] = square * square
        print(f"Output is now: {output}.\n")
    return output


print(main(nums=[-4, -1, 0, 3, 10]))

"""
Output:
Input array: [-4, -1, 0, 3, 10].

Current index is: 4. Comparing left and right index value. Left index 0 and right index 4. 4 < 10.
Current square is: 100.
Output is now: [0, 0, 0, 0, 100].

Current index is: 3. Comparing left and right index value. Left index 0 and right index 3. 4 < 3.
Current square is: 16.
Output is now: [0, 0, 0, 16, 100].

Current index is: 2. Comparing left and right index value. Left index 1 and right index 3. 1 < 3.
Current square is: 9.
Output is now: [0, 0, 9, 16, 100].

Current index is: 1. Comparing left and right index value. Left index 1 and right index 2. 1 < 0.
Current square is: 1.
Output is now: [0, 1, 9, 16, 100].

Current index is: 0. Comparing left and right index value. Left index 2 and right index 2. 0 < 0.
Current square is: 0.
Output is now: [0, 1, 9, 16, 100].

[0, 1, 9, 16, 100]


Time Complexity: O(n)
Space Complexity: O(n) 
"""
