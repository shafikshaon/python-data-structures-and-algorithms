### Problem statement

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers `[1, 3, 4]`  form a subsequence of the array
`[1, 2, 3, 4]`, and so do the numbers `[2, 4]`. Note
that a single number in an array and the array itself are both valid
subsequences of the array.

**Sample Input:**

```
array    = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

**Sample Output:**

```
true
```

### Hint 1

You can solve this question by iterating through the main input array once.

### Hint 2

Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer,
keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue
this process until you either find every integer in the potential subsequence or you reach the end of the main array.

### Hint 3

To actually implement what Hint #2 describes, you'll have to declare a variable holding your position in the potential
subsequence. At first, this position will be the 0th index in the sequence; as you find the sequence's integers in the
main array, you'll increment the position variable until you reach the end of the sequence.

## Optimal Space & Time Complexity

O(n) time | O(1) space - where n is the length of the array

### Test Cases

**Test Case 1**

```
{
  "array": [1, 2, 3, 5, 6, 8, 9]
}
```

**Test Case 2**

```
{
  "array": [1]
}
```

**Test Case 3**

```
{
  "array": [1, 2]
}
```

**Test Case 4**

```
{
  "array": [1, 2, 3, 4, 5]
}
```

**Test Case 5**

```
{
  "array": [0]
}
```

**Test Case 6**

```
{
  "array": [10]
}
```

**Test Case 7**

```
{
  "array": [-1]
}
```

**Test Case 8**

```
{
  "array": [-2, -1]
}
```

**Test Case 9**

```
{
  "array": [-5, -4, -3, -2, -1]
}
```

**Test Case 10**

```
{
  "array": [-10]
}
```

**Test Case 11**

```
{
  "array": [-10, -5, 0, 5, 10]
}
```

**Test Case 12**

```
{
  "array": [-7, -3, 1, 9, 22, 30]
}
```

**Test Case 13**

```
{
  "array": [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
}
```

**Test Case 14**

```
{
  "array": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
```

**Test Case 15**

```
{
  "array": [-1, -1, 2, 3, 3, 3, 4]
}
```

**Test Case 16**

```
{
  "array": [-3, -2, -1]
}
```

**Test Case 17**

```
{
  "array": [-3, -2, -1]
}
```
