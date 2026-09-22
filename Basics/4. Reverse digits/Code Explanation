**Reverse Digits - Code Explanation**

**Correct Code**

```python
class Solution:
    def reverseDigits(self, n):
        return int(str(n)[::-1])
```

**How It Works**

1. Convert the number to a string using `str(n)`.
2. Reverse the string using slicing `[::-1]`.
3. Convert the reversed string back to an integer using `int(...)`.
4. Return the integer.

**Why Leading Zeros Are Removed Automatically**

When reversed digits produce values like `"021"`, converting to `int` gives `21`. So trailing zeros in the original number are naturally dropped after reversal.

**Examples**

- `n = 123` -> `321`
- `n = 540` -> `45`
- `n = 7` -> `7`
- `n = 500` -> `5`

**Complexity**

- Time: `O(d)`, where `d` is the number of digits.
- Space: `O(d)` because of string creation.