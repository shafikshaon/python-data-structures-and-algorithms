class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        print(f"Mid: {mid}. Left: {nums[:mid]}. Right: {nums[mid:]}.\n")
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def sort_array(self, nums):
        print(f"Input array: {nums}.")
        self.merge_sort(nums)
        print(f"\nMerged array: {nums}.")

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        print(
            f"Merged left: {left[i:]}. Merged right: {right[j:]}. Merged combine: {res}."
        )
        return res


sol = Solution()
sol.sort_array(nums=[5, 2, 3, 1])

"""
Output:
Input array: [5, 2, 3, 1].
Mid: 2. Left: [5, 2]. Right: [3, 1].

Mid: 1. Left: [5]. Right: [2].

Merged left: [5]. Merged right: []. Merged combine: [2, 5].
Mid: 1. Left: [3]. Right: [1].

Merged left: [3]. Merged right: []. Merged combine: [1, 3].
Merged left: [5]. Merged right: []. Merged combine: [1, 2, 3, 5].

Merged array: [5, 2, 3, 1].


Time complexity: O(nlog(n))
Space complexity: O(n)
"""
