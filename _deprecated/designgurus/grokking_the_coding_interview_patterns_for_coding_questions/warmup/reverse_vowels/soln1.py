class Solution:
    vowels = "aeiouAEIOU"

    def reverse_vowels(self, s: str) -> str:
        first, last = 0, len(s) - 1
        array = []
        while first < last:
            while first < last and self.vowels.find(array[first]) == -1:
                first += 1
            while first < last and self.vowels.find(array[last]) == -1:
                last -= 1
            array[first], array[last] = array[last], array[first]
            first += 1
            last -= 1
        return "".join(array)


solution = Solution()

s1 = "hello"
expected_output1 = "holle"
actual_output1 = solution.reverse_vowels(s1)
print("Test Case 1: ", expected_output1 == actual_output1)
