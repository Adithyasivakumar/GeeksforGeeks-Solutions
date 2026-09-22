### Prime Number Check

### Step 1: Understand the Problem

- **Input:** A single integer `n`.
- **Output:** A boolean value: `True` if `n` is a prime number, and `False` otherwise.
- **Constraints:** The input `n` can be a very large integer. An efficient solution is required.
- **Definition:** A prime number is a natural number **greater than 1** that has no positive divisors other than 1 and itself.

---

### Step 2: Work Through Examples

- **Example 1:**
    - **Input:** `n = 7`
    - **Output:** `True` (Explanation: 7's only divisors are 1 and 7.)
- **Example 2:**
    - **Input:** `n = 25`
    - **Output:** `False` (Explanation: 25 is divisible by 5, so it is not prime.)
- **Example 3:**
    - **Input:** `n = 1`
    - **Output:** `False` (Explanation: By definition, prime numbers must be greater than 1.)
- **Example 4:**
    - **Input:** `n = 2`
    - **Output:** `True` (Explanation: 2 is the smallest prime number.)

---

### Step 3: Identify the Problem Type

- Number Theory
- Algorithm Optimization
- Mathematical Logic

---

### Step 4: Think About Approaches

- **Brute Force (Naive):** Iterate from `i = 2` all the way to `n - 1`. If `n` is divisible by any `i` in that range, it is not prime. If the loop finishes, it is prime. This approach is simple to understand but extremely slow for large numbers (e.g., `n = 10^9`) and will fail due to "Time Limit Exceeded" errors.
- **Optimal Approach (Square Root Optimization):** Factors of a number come in pairs. For example, the factors of 36 are (2, 18), (3, 12), (4, 9), and (6, 6). Notice that in each pair `(a, b)`, one number is always less than or equal to the square root (`√36 = 6`). Therefore, we only need to check for divisors up to `√n`. If we find a divisor, we know the number isn't prime. If we don't find any, it must be prime. This is drastically faster.

---

### Step 5: Plan Before Coding

- **Pseudocode:**
    
    `function isPrime(n):
      // 1. Handle base cases based on the definition of a prime.
      If n <= 1:
        Return False
    
      // 2. Iterate from 2 up to the square root of n.
      Loop i from 2 up to floor(sqrt(n)):
        // 3. Check for divisibility.
        If n % i == 0:
          // A factor was found, so it's not prime.
          Return False
    
      // 4. If the loop completes, no factors were found.
      Return True`
    

---

### Step 6: Consider Edge Cases

- **`n = 0`, `n = 1`:** These are not prime. The initial `if n <= 1:` check handles this correctly.
- **`n = 2`:** The smallest prime. The loop `range(2, int(√2)+1)` becomes `range(2, 2)`, which is empty. The function correctly skips the loop and returns `True`.
- **Small composite numbers:** For `n = 9`, the loop runs up to `int(√9) = 3`. It checks `i = 2` (no) and then `i = 3`. Since `9 % 3 == 0`, it correctly returns `False`.
- **Large prime numbers:** For a large prime, the loop will run up to its square root and find no divisors, correctly returning `True` without timing out.

---

### Step 7: Complexity Analysis

- **Time Complexity: O(√n)**
    - The number of loop iterations is determined by the square root of `n`. This is highly efficient and fast enough for large inputs.
- **Space Complexity: O(1)**
    - The algorithm uses a constant amount of extra memory to store variables like `i`. The space required does not grow as `n` grows.

---

### Step 8: Review and Reflect

- **Why does this work?** The algorithm's correctness hinges on the mathematical property that any composite number `n` must have a prime factor less than or equal to `√n`. By only checking up to this limit, we eliminate a massive number of unnecessary checks required by the naive approach, without sacrificing accuracy.
- **Can it be improved?** While O(√n) is excellent, minor optimizations are possible (e.g., checking 2 separately and then only checking odd numbers). However, for the given constraints, this approach is the standard and accepted optimal solution. More advanced algorithms like the Sieve of Eratosthenes are used for finding *all primes* in a range, which is a different problem.