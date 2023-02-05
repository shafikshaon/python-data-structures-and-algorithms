class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0

        for idx in range(len(s)):
            print(
                f"Current idx: {idx}, k = {k}. Frequency map at idx ({idx}) value: {s[idx]}."
            )
            frequency_map[s[idx]] = frequency_map.get(s[idx], 0) + 1
            print(f"Frequency map: {frequency_map}.")

            max_frequency = max(max_frequency, frequency_map[s[idx]])
            print(f"Max frequency: {max_frequency}.")

            is_valid = idx + 1 - start - max_frequency <= k
            print(f"Is valid: {is_valid}.")
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1
            longest_substring_length = idx + 1 - start
            print(
                f"Longest substring length: {longest_substring_length}. "
                f"Frequency now: {frequency_map}.\n"
            )
        print(f"\nThe final longest substring length: {longest_substring_length}.")
        return longest_substring_length


sol = Solution()
print(f'Output: {sol.characterReplacement(s="ABAB", k=1)}')

"""
Output:
Current idx: 0, k = 2. Frequency map at idx (0) value: A.
Frequency map: {'A': 1}.
Max frequency: 1.
Is valid: True.
Longest substring length: 1. Frequency now: {'A': 1}.

Current idx: 1, k = 2. Frequency map at idx (1) value: B.
Frequency map: {'A': 1, 'B': 1}.
Max frequency: 1.
Is valid: True.
Longest substring length: 2. Frequency now: {'A': 1, 'B': 1}.

Current idx: 2, k = 2. Frequency map at idx (2) value: A.
Frequency map: {'A': 2, 'B': 1}.
Max frequency: 2.
Is valid: True.
Longest substring length: 3. Frequency now: {'A': 2, 'B': 1}.

Current idx: 3, k = 2. Frequency map at idx (3) value: B.
Frequency map: {'A': 2, 'B': 2}.
Max frequency: 2.
Is valid: True.
Longest substring length: 4. Frequency now: {'A': 2, 'B': 2}.


The final longest substring length: 4.
Output: 4

Time Complexity: O(n)
Space Complexity: O(m), Considering uppercase English letters only, m=26.
"""
