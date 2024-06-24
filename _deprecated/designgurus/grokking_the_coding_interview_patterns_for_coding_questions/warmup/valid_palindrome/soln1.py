class Solution:
    def is_palindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1
        while first < last:
            while first < last and not s[first].isalnum():
                first += 1
            while first < last and not s[last].isalnum():
                last -= 1
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True


solution = Solution()

s1 = "A man, a plan, a canal, Panama!"
actual_output1 = solution.is_palindrome(s1)
print(actual_output1)
