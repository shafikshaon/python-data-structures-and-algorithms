class Solution:
    def shortestDistance(self, words, word1, word2):
        shortestDistance = len(words)
        position1, position2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                position1 = i
            if word == word2:
                position2 = i
            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))
        return shortestDistance


solution = Solution()
# Test case 1
words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
word11 = "fox"
word21 = "dog"
expected_output1 = 5
actual_output1 = solution.shortestDistance(words1, word11, word21)
print("Test case 1:", expected_output1 == actual_output1)
