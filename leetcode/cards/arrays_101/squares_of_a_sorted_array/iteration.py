def main(nums):
    output = []
    for n in nums:
        squared_num = n ** 2
        output.append(squared_num)
    return sorted(output)


print(main(nums=[-4, -1, 0, 3, 10]))
print(main(nums=[-7, -3, 2, 3, 11]))

"""
Output:
[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]

Time Complexity: O(nlog(n))
Space Complexity: O(nlog(n)) # https://wiki.python.org/moin/TimeComplexity
"""
