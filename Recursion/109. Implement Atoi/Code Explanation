# **Problem Explanation**

## **Implement Atoi**

### **Step 1: Understand the Problem**

- **Input:** A string `s`.
- **Output:** The 32-bit signed integer value derived from the string.
- **Goal:** Replicate the behavior of the C/C++ `atoi` function.
- **Rules:**
    1. **Whitespace:** Ignore leading whitespace.
    2. **Sign:** Check for `+` or  immediately after whitespace.
    3. **Digits:** Read consecutive digits until a non-digit character is encountered or the end of the string.
    4. **Garbage:** Ignore any characters after the valid number.
    5. **Clamping:** If the result exceeds 231−1 or is less than −231, return the respective limit.

### **Step 2: Work Through Examples**

- **Example 1:** `"42"`
    - No whitespace, no sign (positive). Read 4, 2.
    - **Output:** `42`.
- **Example 2:** `" -42"`
    - Strip spaces. Found . Read 4, 2. Apply sign.
    - **Output:** `42`.
- **Example 3:** `"4193 with words"`
    - Read 4, 1, 9, 3. Stop at space `' '`.
    - **Output:** `4193`.
- **Example 4:** `"words and 987"`
    - First char `w` is not a digit or sign. Stop immediately.
    - **Output:** `0`.
- **Example 5 (Overflow):** `"-91283472332"`
    - Number is smaller than −231.
    - **Output:** `2147483648`.

### **Step 3: Identify the Problem Type**

- **String Manipulation / Parsing**
- **Simulation** (Simulating a Finite State Machine)
- **Math** (Digit assembly and Overflow handling)

### **Step 4: Think About Approaches**

- **Native Casting (`int(s)`):**
    - *Critique:* Fails on inputs like `"42 words"`. We need manual parsing.
- **Linear Scan (The Solution):**
    - Process the string character by character from left to right.
    - Maintain a strict order of operations: **Clean -> Sign -> Build -> Clamp**.
    - Once we enter the "Digit building" phase, any non-digit stops the process entirely.

### **Step 5: Plan Before Coding**

**Pseudocode:**

Plaintext

`function myAtoi(s):
    1. Strip leading/trailing whitespaces.
    2. If string is empty, return 0.
    
    3. Check first character for Sign (+ or -).
       - Record sign (+1 or -1).
       - Remove sign character from string to simplify loop.

    4. Loop through remaining characters:
       - If char is digit:
         result = result * 10 + int(char)
       - If char is NOT digit:
         Break loop immediately.

    5. Apply Sign to result.

    6. Clamp result:
       - If result > 2^31 - 1, return 2^31 - 1
       - If result < -2^31, return -2^31
    
    7. Return result.`

### **Step 6: Consider Edge Cases**

- **`""` or `" "`:** Becomes empty after strip. Returns 0. Correct.
- **`"-"` or `"+"`:** Sign logic runs, string becomes empty. Loop doesn't run. Returns 0. Correct.
- **`"000042"`:** Zeros are read as digits. `0 * 10 + 0` remains 0 until `4` is hit. Returns `42`. Correct.

### **Step 7: Complexity Analysis**

- **Time Complexity:** O(N). We scan the string once (technically twice due to `strip()`).
- **Space Complexity:** O(N) in this Python implementation because `s.strip()` and `s[1:]` create new string copies.
    - *Note:* Can be optimized to O(1) by using index pointers instead of slicing.

### **Step 8: Review and Reflect**

- **Why does this work?** It acts like a state machine. We strictly transition from "Waiting for Start" → "Reading Sign" → "Reading Digits" → "Done". The mathematical formula `result = result * 10 + digit` is the standard way to construct integers from a stream of digits.

---

# **Code Explanation**

### **The Analogy: The Strict Form Filler**

Imagine you are filling out a government form box that asks for "Amount Earned".

1. **Ignore Smudges:** You ignore the empty space at the start (`strip`).
2. **Check Tone:** You look for a minus sign to see if it's debt (`sign`).
3. **Read Carefully:** You write down numbers one by one. The moment you see a letter, a symbol, or a coffee stain, **you stop writing**. You don't look ahead for more numbers.
4. **The Box Limit:** If the number you wrote is bigger than what fits in the box (32-bit), you just write the maximum possible value the box allows.

### **Step 1: Cleaning & Edge Case**

**Code:**

Python

        `s = s.strip()
        if not s:
            return 0`

- **What it does:** Removes spaces. If the string was just `" "`, it becomes empty, so we return 0 safely to avoid errors accessing index 0 later.

### **Step 2: Handling the Sign**

**Code:**

Python

        `sign = 1
        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                sign = -1
            s = s[1:]`

- **What it does:** Checks if the number is explicitly positive or negative.
- **Slicing:** `s = s[1:]` removes the sign from the string so the upcoming loop only has to worry about digits.

### **Step 3: Building the Number**

**Code:**

Python

        `for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)`

- **What it does:**
    - **The Check:** If we hit a letter (e.g., `'a'`), we `break` immediately. We don't skip it; we stop.
    - **The Math:** `result * 10` shifts the current digits to the left (e.g., `4` becomes `40`), and `+ int(char)` adds the new digit to the ones place (`40 + 2 = 42`).

### **Step 4: Clamping (Overflow Handling)**

**Code:**

Python

        `result = result * sign
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31`

- **What it does:** Applies the sign, then checks if the number violates the 32-bit integer range. If it does, it caps the value at the boundary.

---

# **Analysis Summary (Deep Revision Framework)**

### **The Core Idea:**

The one-sentence summary is: **"We simulate a Finite State Machine that parses the string in a strict order (Whitespace → Sign → Digits), constructing the integer mathematically while discarding invalid trailing characters and clamping the result to 32-bit limits."**

### **Data Structure Choice:**

- **String:** The input medium.
- **Integer:** The accumulator for the result.

### **Algorithm Pattern:**

- **Linear Scan / Simulation:** Processing input sequentially based on a set of rules.

### **Complexity:**

- **Time:** O(N).
- **Space:** O(N) (due to string slicing).

### **Articulate the Solution:**

"I implemented a parser that first sanitizes the input by stripping whitespace."
"I checked for an optional sign character and stored it."
"Then, I iterated through the string, constructing the number digit-by-digit (`res * 10 + digit`) and stopping immediately upon encountering a non-digit."
"Finally, I applied the sign and clamped the result to the 32-bit integer range."

### **Spaced Repetition & Follow-ups:**

- **Optimization:** "How to reduce space to O(1)?"
    - **Answer:** Instead of `s.strip()` and `s[1:]`, use an index pointer `i` to skip spaces and the sign, and iterate through the original string.
- **Edge Case:** "What happens with `+-42`?"
    - **Answer:** The logic sees `+` as sign, removes it. Then it sees .  is not a digit. Loop breaks. Returns `0`.

---

# **Key Notes**

- **Order Matters:** You cannot check for the sign *inside* the loop efficiently. It must be done exactly once, before digit processing starts.
- **The Break:** The `break` statement is crucial. `atoi` does not skip bad characters; it terminates parsing.
- **Large Integers:** Python handles arbitrarily large integers, so we can store the result and check limits at the end. In languages like C++ or Java, we would need to check for overflow *before* multiplying by 10 inside the loop.