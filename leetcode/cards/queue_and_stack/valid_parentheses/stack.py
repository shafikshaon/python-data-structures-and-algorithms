def main(s):
    bracket_mapping = {"(": ")", "{": "}", "[": "]"}
    open_brackets = ["(", "{", "["]

    stack = []

    for i in s:
        if i in open_brackets:
            print(f'Pushing "{i}" in stack.')
            stack.append(i)
        elif stack and bracket_mapping[stack[-1]] == i:
            print(
                f"Current stack is: {stack}. The last item in stack {stack[-1]}. The current bracket is {i}."
            )
            stack.pop()
        else:
            return False
        print(f"Now stack is: {stack}.")
    print(f"Is valid parentheses? {stack == []}.")
    return stack == []


main(s="()[]{}")
print(
    "-----------------------------------------------------------------------------------------------------"
)
main(s="()[]{}()[]{}()[]{}()[]{}[")

"""
Output:
Pushing "(" in stack.
Now stack is: ['('].
Current stack is: ['(']. The last item in stack (. The current bracket is ).
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Current stack is: ['[']. The last item in stack [. The current bracket is ].
Now stack is: [].
Pushing "{" in stack.
Now stack is: ['{'].
Current stack is: ['{']. The last item in stack {. The current bracket is }.
Now stack is: [].
Is valid parentheses? True.
-----------------------------------------------------------------------------------------------------
Pushing "(" in stack.
Now stack is: ['('].
Current stack is: ['(']. The last item in stack (. The current bracket is ).
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Current stack is: ['[']. The last item in stack [. The current bracket is ].
Now stack is: [].
Pushing "{" in stack.
Now stack is: ['{'].
Current stack is: ['{']. The last item in stack {. The current bracket is }.
Now stack is: [].
Pushing "(" in stack.
Now stack is: ['('].
Current stack is: ['(']. The last item in stack (. The current bracket is ).
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Current stack is: ['[']. The last item in stack [. The current bracket is ].
Now stack is: [].
Pushing "{" in stack.
Now stack is: ['{'].
Current stack is: ['{']. The last item in stack {. The current bracket is }.
Now stack is: [].
Pushing "(" in stack.
Now stack is: ['('].
Current stack is: ['(']. The last item in stack (. The current bracket is ).
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Current stack is: ['[']. The last item in stack [. The current bracket is ].
Now stack is: [].
Pushing "{" in stack.
Now stack is: ['{'].
Current stack is: ['{']. The last item in stack {. The current bracket is }.
Now stack is: [].
Pushing "(" in stack.
Now stack is: ['('].
Current stack is: ['(']. The last item in stack (. The current bracket is ).
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Current stack is: ['[']. The last item in stack [. The current bracket is ].
Now stack is: [].
Pushing "{" in stack.
Now stack is: ['{'].
Current stack is: ['{']. The last item in stack {. The current bracket is }.
Now stack is: [].
Pushing "[" in stack.
Now stack is: ['['].
Is valid parentheses? False.
"""


"""
Time complexity: O(n)
Space complexity: O(n)
"""
