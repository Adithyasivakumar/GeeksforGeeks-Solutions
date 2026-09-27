## **Find Last Digit Of a^b for Large Numbers**

**Step 1: Understand the Problem**

- **Input:** Two large numbers, `a` (the base) and `b` (the exponent), given as strings.
- **Output:** The single last digit of the number `a` raised to the power of `b`.
- **Core Challenge:** The numbers `a` and `b` are given as strings because they can be too large to fit into standard integer types. Directly calculating `int(a) ** int(b)` is impossible because the result would be a gigantic number.

---

**Step 2: Work Through Examples**

- **Example 1: `a = "3", b = "10"`**
    - We need the last digit of 3¹⁰.
    - 3¹⁰ = 59049.
    - The last digit is **9**.
- **Example 2: `a = "2", b = "5"`**
    - We need the last digit of 2⁵.
    - 2⁵ = 32.
    - The last digit is **2**.
- **Pattern Recognition:** By looking at powers, we see that the last digits repeat in a cycle.
    - Powers of 2 end in: 2, 4, 8, 6, 2, 4, 8, 6... (a cycle of length 4)
    - Powers of 3 end in: 3, 9, 7, 1, 3, 9, 7, 1... (a cycle of length 4)

---

**Step 3: Identify the Problem Type**

- Mathematical Problem
- **Modular Arithmetic**
- **Pattern Recognition / Cyclicity**

---

**Step 4: Think About Approaches**

- **Brute-Force:** Calculate the full value of `a^b`. This is infeasible due to the enormous size of the numbers.
- **Optimal Approach (Cyclicity):** This is the correct solution. It's based on two key insights:
    1. The last digit of `a^b` only depends on the last digit of `a`.
    2. The pattern of these last digits repeats in a cycle of 4 (or a divisor of 4).
    This allows us to solve the problem using only small, manageable numbers.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function getLastDigit(a, b):
      // 1. Handle the base case where the exponent is "0".
      if b is "0", return 1.
    
      // 2. We only need the last digit of the base `a`.
      last_digit_a = integer of the last character of string a.
    
      // 3. Calculate the effective exponent by finding `b % 4`.
      //    Since `b` is a huge string, we do this digit by digit.
      effective_exponent = remainder of (b as an integer) when divided by 4.
    
      // 4. If the remainder is 0, it corresponds to the 4th position in the cycle.
      if effective_exponent is 0, set it to 4.
    
      // 5. Calculate the power using these small numbers.
      result = last_digit_a raised to the power of effective_exponent.
    
      // 6. Return the last digit of this small result.
      return result % 10.`
    

---

**Step 6: Consider Edge Cases**

- **`b = "0"`:** Any number to the power of 0 is 1. The code must handle this and return 1.
- **`a` ends in 0, 1, 5, or 6:** These numbers have very simple cycles of length 1. The logic still works for them.
- **`b` is a multiple of 4:** The remainder `b % 4` will be 0. This corresponds to the 4th (last) element of the cycle, so the effective exponent must be treated as 4.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(|b|)**, where |b| is the length of the string `b`. This is dominated by the loop that iterates through the digits of `b` to calculate the remainder modulo 4.
- **Space Complexity: O(1)**. The algorithm uses only a few variables, regardless of the input size.

---

**Step 8: Review and Reflect**

- **Why does this work?** The solution brilliantly avoids dealing with impossibly large numbers by using a fundamental mathematical property: the **cyclicity** of last digits. By using modular arithmetic to find the number's position within this short cycle, a computationally hard problem is reduced to a simple calculation with single-digit numbers.
- **Can it be improved?** The logic is optimal. The O(|b|) time complexity is necessary to correctly parse the exponent `b` when it's given as a string.