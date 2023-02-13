**Problem Number:** #0001

**Problem Link:** https://leetcode.com/problems/two-sum/

**Difficulty:** Easy

**Tag:** `Array`, `Hash Table`

**Problem Statement:** Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same
element twice. You can return the answer in any order.

**Input:** nums = [2,7,11,15], target = 9

**Output:** [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

## Solution 1

### Brute Force Approach

This is a basic implementation of the Two-Sum problem. The Two-Sum problem is to find two numbers in an array that add
up to a target value.

This implementation uses nested loops to compare each number with every other number. The outer loop iterates over the
elements of the input array `nums` starting from index 0, and the inner loop starts from the index `i + 1` to avoid
duplicate results.

For each iteration, the current number from the outer loop and the target value are used to calculate the desired value
of the other number, and if the desired value is found in the input array, the indices of the two numbers are returned
as the solution.

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


sol = Solution()
output = sol.twoSum(nums=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
print(f"Output: {output}.")
```

    Output: [4, 6].

**Time Complexity:** $O(n^2)$

**Space Complexity:** $O(1)$

## Solution 2

### Two-pass Hash Table

The given code implements the "Two Sum" problem solution using a hash map.

1. The first for loop populates the hash map by iterating through the list of numbers "nums" and storing each number and
   its index as a key-value pair in the hash map.

2. The second for loop iterates through the "nums" list again and for each number, it calculates its complement (the
   number needed to add up to the target value) by subtracting the current number from the target.

3. It then checks if the complement exists in the hash map and if it does, and the index of the complement is not the
   same as the current number, it returns a list of the indices of the two numbers that add up to the target.

The time complexity of this solution is O(n) since it iterates through the "nums" list twice. The space complexity is O(
n) since the hash map stores up to n key-value pairs.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        print(f"Hash map now: {hash_map}.")
        for i in range(len(nums)):
            complement = target - nums[i]
            print(f"i = {i}, complement = {complement}.")
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]


sol = Solution()
output = sol.twoSum(nums=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
print(f"Output: {output}.")
```

    Hash map now: {3: 0, 5: 1, -4: 2, 8: 3, 11: 4, 1: 5, -1: 6, 6: 7}.
    i = 0, complement = 7.
    i = 1, complement = 5.
    i = 2, complement = 14.
    i = 3, complement = 2.
    i = 4, complement = -1.
    Output: [4, 6].

**Time Complexity:** $O(n)$

**Space Complexity:** $O(n)$

## Solution 3

### One-pass Hash Table

The given implementation is for finding the two indices of numbers in an array `nums` such that when added together,
their sum is equal to the `target`.

The approach uses a hash-map to store the numbers in the array as keys and their indices as values.

The algorithm iterates over each number in the array and calculates its complement, which is `target - nums[i]`. If the
complement exists in the hash-map, it means that there is a pair of numbers in the array whose sum is equal to the
target. The two indices of those numbers are `i` and `hash_map[complement]` and they are returned.

If the complement does not exist in the hash-map, the current number is added to the hash-map with its index as the
value.

The time complexity of this solution is O(n) and space complexity is O(n) as well, where n is the number of elements in
the input array `nums`.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[nums[i]] = i


sol = Solution()
output = sol.twoSum(nums=[3, 5, -4, 8, 11, 1, -1, 6], target=10)
print(f"Output: {output}.")
```

    Output: [6, 4].

**Time Complexity:** $O(n)$

**Space Complexity:** $O(n)$

