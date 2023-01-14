def main(s: str, t: str) -> bool:
    left_bound = len(s)
    right_bound = len(t)

    left = right = 0

    while left < left_bound and right < right_bound:
        print(
            f'Left pointer "{left}" and value from string s is: "{s[left]}" , right pointer "{right}" and value from string t is: "{t[right]}".'
        )
        if s[left] == t[right]:
            left += 1
        right += 1

    print(
        f"left = {left} and left string length {left_bound}. So return {left == left_bound}."
    )
    return left == left_bound


main(s="abc", t="ahbgdc")
print("-----------------------------------------------------------------------------------------------------")
main(s="axc", t="ahbgdc")

# Time complexity: O(n)
# Space complexity: O(1)

# Output
"""
Left pointer "0" and value from string s is: "a" , right pointer "0" and value from string t is: "a".
Left pointer "1" and value from string s is: "b" , right pointer "1" and value from string t is: "h".
Left pointer "1" and value from string s is: "b" , right pointer "2" and value from string t is: "b".
Left pointer "2" and value from string s is: "c" , right pointer "3" and value from string t is: "g".
Left pointer "2" and value from string s is: "c" , right pointer "4" and value from string t is: "d".
Left pointer "2" and value from string s is: "c" , right pointer "5" and value from string t is: "c".
left = 3 and left string length 3. So return True.
-----------------------------------------------------------------------------------------------------
Left pointer "0" and value from string s is: "a" , right pointer "0" and value from string t is: "a".
Left pointer "1" and value from string s is: "x" , right pointer "1" and value from string t is: "h".
Left pointer "1" and value from string s is: "x" , right pointer "2" and value from string t is: "b".
Left pointer "1" and value from string s is: "x" , right pointer "3" and value from string t is: "g".
Left pointer "1" and value from string s is: "x" , right pointer "4" and value from string t is: "d".
Left pointer "1" and value from string s is: "x" , right pointer "5" and value from string t is: "c".
left = 1 and left string length 3. So return False.
"""
