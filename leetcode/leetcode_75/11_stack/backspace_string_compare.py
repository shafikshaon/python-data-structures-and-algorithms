class Solution:
    def build(self, string):
        ans = []
        for c in string:
            if c != "#":
                print(f'Appending "{c}" to ans: {ans}.')
                ans.append(c)
                print(f"After appending, the ans is: {ans}.")
            elif ans:
                print(f"Applying backspace...")
                ans.pop()
                print(f"After backspace, the ans is: {ans}.")
        return "".join(ans)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)


sol = Solution()
sol.backspaceCompare(s="ab#c", t="ad#c")

"""
Output:
Appending "a" to ans: [].
After appending, the ans is: ['a'].
Appending "b" to ans: ['a'].
After appending, the ans is: ['a', 'b'].
Applying backspace...
After backspace, the ans is: ['a'].
Appending "c" to ans: ['a'].
After appending, the ans is: ['a', 'c'].
Appending "a" to ans: [].
After appending, the ans is: ['a'].
Appending "d" to ans: ['a'].
After appending, the ans is: ['a', 'd'].
Applying backspace...
After backspace, the ans is: ['a'].
Appending "c" to ans: ['a'].
After appending, the ans is: ['a', 'c'].


Time Complexity: O(m + n)
Space Complexity: O(m + n)
"""
