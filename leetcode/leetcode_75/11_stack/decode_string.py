class Solution:
    def decodeString(self, s: str) -> str:
        print(f"Input string: {s}.\n")
        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                # In between the square brackets, it will always be a string
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop()

                # After the opening square bracket, it will always be a number
                digit = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    digit = stack.pop() + digit
                print(f'String: "{sub_str}" and multiplied {digit} times.')
                sub_str *= int(digit)
                stack.append(sub_str)
                print(f"Now stack is: {stack}.\n")
            else:
                stack.append(s[i])
                print(f'Appending "{s[i]}" to stack. Now stack is: {stack}.')
        return "".join(stack)


sol = Solution()
print(f'\nOutput: {sol.decodeString(s="3[a]2[bc]")}')

"""
Output:
Input string: 3[a]2[bc].

Appending "3" to stack. Now stack is: ['3'].
Appending "[" to stack. Now stack is: ['3', '['].
Appending "a" to stack. Now stack is: ['3', '[', 'a'].
String: "a" and multiplied 3 times.
Now stack is: ['aaa'].

Appending "2" to stack. Now stack is: ['aaa', '2'].
Appending "[" to stack. Now stack is: ['aaa', '2', '['].
Appending "b" to stack. Now stack is: ['aaa', '2', '[', 'b'].
Appending "c" to stack. Now stack is: ['aaa', '2', '[', 'b', 'c'].
String: "bc" and multiplied 2 times.
Now stack is: ['aaa', 'bcbc'].


Output: aaabcbc


Time Complexity: O(n)
Space Complexity: O(n)
"""
