def is_even_number_digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count % 2 == 0


def main(nums):
    even_number_count = 0
    for n in nums:
        if is_even_number_digit(n):
            even_number_count += 1
    return even_number_count


print(main(nums=[12, 345, 2, 6, 7896]))
print(main(nums=[555, 901, 482, 1771]))

"""
Output:
2
1

Time Complexity: O(n)
Space Complexity: O(1)
"""
