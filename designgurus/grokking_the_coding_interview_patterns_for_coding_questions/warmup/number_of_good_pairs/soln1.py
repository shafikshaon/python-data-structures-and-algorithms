class Solution:
    def numGoodPairs(self, nums):
        pair_count = 0
        hash_map = {}
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
            pair_count += hash_map[n] - 1
        return pair_count


sol = Solution()
nums1 = [1, 2, 3, 1, 1, 3]
result1 = sol.numGoodPairs(nums1)
print("Result 1:", result1, "(Expected: 4)")
