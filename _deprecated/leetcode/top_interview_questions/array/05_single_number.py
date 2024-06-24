from typing import List


def main(nums: List[int]) -> int:
    print(f"Original array: {nums}\n")
    a: int = 0
    for i in nums:
        print(f"Current number is: {i} and after applying XOR ({a} ^ {i}): {a ^ i}")
        print(f"{a:08b}")
        print(f"{i:08b}")
        print("--------")
        print(f"{a ^ i:08b} ({a ^ i})")
        print("")
        a ^= i
    return a


main(nums=[4, 1, 1])

# Time complexity - O(n)
# Space complexity - O(1)
