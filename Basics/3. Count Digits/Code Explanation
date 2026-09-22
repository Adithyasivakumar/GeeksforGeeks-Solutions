## **Count Digits**

**Step 1: Understand the Problem**

- **Input:** A single positive integer `n`.
- **Output:** An integer that represents a count.
- **Goal:** To count how many of the individual digits *within* the number `n` are able to divide `n` evenly (i.e., with a remainder of 0).
- **Special Rule:** The digit 0 must be ignored, as division by zero is undefined and would cause an error.

---

**Step 2: Work Through Examples**

- **Example 1: `n = 12`**
    - The digits are 1 and 2.
    - Is `12 % 1 == 0`? Yes.
    - Is `12 % 2 == 0`? Yes.
    - The total count of such digits is 2.
    - **Output: 2**
- **Example 2: `n = 23`**
    - The digits are 2 and 3.
    - Is `23 % 2 == 0`? No.
    - Is `23 % 3 == 0`? No.
    - The total count is 0.
    - **Output: 0**

---

**Step 3: Identify the Problem Type**

- Number Manipulation
- Digit Extraction
- Looping and Conditionals

---

**Step 4: Think About Approaches**

- **String Conversion (The Implemented Solution):** Convert the number `n` to a string to easily loop through its characters. For each character, convert it back to an integer to perform the mathematical division check. This approach is very intuitive and easy to read.
- **Arithmetic Method:** Use a `while` loop with the modulo (`% 10`) and floor division (`// 10`) operators to extract digits mathematically without any type conversion. This is also a very common and efficient pattern.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function evenlyDivides(n):
      // 1. Save the original number, because we need it for the division check.
      original_n = n
    
      // 2. Convert the number to a string to easily access its digits.
      n_as_string = string(n)
    
      // 3. Initialize a counter to store the result.
      count = 0
    
      // 4. Loop through each character of the string.
      For each digit_character in n_as_string:
        // 5. Convert the character back into a number.
        digit = integer(digit_character)
    
        // 6. Check the two required conditions.
        if digit is not 0 AND original_n is divisible by digit:
          // 7. If both conditions are met, increment the counter.
          increment count
    
      // 8. Return the final count.
      return count`
    

---

**Step 6: Consider Edge Cases**

- **Single-digit number `n = 7`:** The original number is 7. The only digit is 7. `7 != 0` and `7 % 7 == 0`. The count becomes 1. The function correctly returns 1.
- **Number containing a zero `n = 105`:** The original number is 105.
    - Digit 1: `105 % 1 == 0`. Count = 1.
    - Digit 0: The `if digit != 0` check correctly causes this digit to be skipped, preventing a `ZeroDivisionError`.
    - Digit 5: `105 % 5 == 0`. Count = 2.
    - The function correctly returns 2.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(log10(N))** or **O(d)**, where `d` is the number of digits in N. The amount of work (the loop) depends on the number of digits, not the value of N itself.
- **Space Complexity: O(log10(N))** or **O(d)**. The string `string_n` requires space proportional to the number of digits in N.

---

**Step 8: Review and Reflect**

- **Why does this work?** The solution correctly translates the problem's rules into code. It uses a simple method (string conversion) to access the digits. It carefully saves the original value of `n` for the division check and includes the crucial safety check to ignore the digit 0.
- **Can it be improved?** The solution is clear and efficient enough for the problem's constraints. An alternative arithmetic-based approach would use O(1) space, but the string conversion method is often considered more readable.