# Problem Explanation

## First Negative in Windows of Size K

## Step 1: Understand the Problem

- **Input:** An integer array `arr` and an integer `k`.
- **Output:** An array containing the first negative integer for each contiguous subarray of size `k`. If a window does not contain a negative integer, output `0`.
- **Definition:** As you slide a fixed window across the array, you must instantly identify the first negative number reading from left to right *within that specific window*.
- **Goal:** Avoid scanning the entire window of size `k` from scratch on every step. Maintain a running record of negative numbers so you can fetch the answer in strictly O(1) time per window.

## Step 2: Work Through Examples

- **Example 1:**
    - `arr` = `[12, -1, -7, 8, -15, 30, 16, 28]`, `k = 3`
    - *Window 1:* `[12, -1, -7]`. First negative is `1`.
    - *Window 2:* `[-1, -7, 8]`. First negative is `1`.
    - *Window 3:* `[-7, 8, -15]`. First negative is `7`.
    - *Window 4:* `[8, -15, 30]`. First negative is `15`.
    - *Window 5:* `[-15, 30, 16]`. First negative is `15`.
    - *Window 6:* `[30, 16, 28]`. No negatives! Output `0`.
    - **Output:** `[-1, -1, -7, -15, -15, 0]`

## Step 3: Identify the Problem Type

- **Sliding Window + Queue:** Because you only care about the *first* negative number, you need a First-In, First-Out (FIFO) data structure to track the order in which negative numbers appear.

## Step 4: Think About Approaches

- **Brute Force (O(N×K) Time):** Run a nested loop. For every window, scan from its start index to its end index until you find a negative number.
    - *Critique:* If the array has very few negative numbers, the inner loop scans all K elements repeatedly, wasting massive compute time.
- **Sliding Window with Deque (O(N) Time, O(K) Space):** This is your provided code.
    - Use a double-ended queue to store *only* the negative numbers.
    - When sliding the window, append incoming negatives to the queue. If the outgoing element is a negative number, it must be the one at the front of the queue, so you pop it.
    - *Critique:* This is the optimal, industry-standard approach. It perfectly applies the O(1) mathematical slide update to a data structure instead of an accumulator!

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```python
function firstNegInt(arr, k):
// 1. Setup
q = empty deque
ans = empty list

// 2. Process Initial Window
for first k elements:
    if element is negative, push to q
record front of q (or 0) into ans

// 3. Slide the Window
for i from k to end of arr:
    incoming = arr[i]
    outgoing = arr[i - k]

    // Update State
    if incoming is negative: push to q
    if outgoing is negative: pop front of q

    // Record
    record front of q (or 0) into ans

return ans
```

## Step 6: Consider Edge Cases

- **No Negatives in a Window:** Your ternary-style check `q[0] if q else 0` perfectly handles windows that consist entirely of positive numbers, preventing `IndexError`s.
- **Multiple Identical Negatives:** If the array is `[-8, -8, 2]`, `q` holds both `[-8, -8]`. When the first `8` slides out of the window, `q.popleft()` removes only the first one, leaving the second `8` safely in the queue. The FIFO properties handle duplicates flawlessly.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). You process the first K elements, then the remaining N−K elements exactly once. Appending to a `deque` and popping from the left of a `deque` are strictly O(1) operations.
- **Space Complexity:** O(K) auxiliary space. The queue will store at most K elements if every single number inside the current window happens to be negative.

## Step 8: Review and Reflect

- **Loop Structure Mastery:** You perfectly implemented the `for i in range(k, len(arr))` loop structure with the `arr[i - k]` outgoing element logic discussed in the previous distinct-element problem. This proves a rock-solid grasp of the fixed sliding window template!

# Code Explanation

## The Analogy: The Complaint Line

Imagine a line of `k` people standing at a service desk. Most people are happy (positive numbers), but some are angry (negative numbers). The manager only wants to talk to the *first* angry person in the line.
Instead of scanning the whole line every time, the manager keeps a separate VIP Complaint Queue (`q`). Whenever an angry person joins the main line, they are also added to the back of the Complaint Queue.
When the person at the front of the main line finishes and leaves (`outgoing`), the manager checks if they were an angry person. If they were, they are also removed from the front of the Complaint Queue (`q.popleft()`).
At any given moment, the manager just looks at the person standing at the very front of the Complaint Queue (`q[0]`). That person is mathematically guaranteed to be the first angry person currently standing in the main line!

## Step 1: Initializing the First Window

Python

```python
q = deque()
ans = []

for i in range(k):
    if arr[i] < 0:
        q.append(arr[i])

ans.append(q[0] if q else 0)
```

- **What it does:** Sweeps the first window of size `k`. It filters out all positive numbers, storing only the negative numbers in the deque to preserve their chronological order. It then records the first negative number found (or `0` if the deque is empty) into the answer array.

## Step 2: Sliding the Pointers

Python

```python
for i in range(k, len(arr)):
    incoming = arr[i]
    outgoing = arr[i - k]
```

- **What it does:** Starts the main sliding sequence. It instantly identifies which new element is entering the right side of the window and which old element is falling out of the left side.

## Step 3: State Updates

Python

```python
    if incoming < 0:
        q.append(incoming)

    if outgoing < 0 and q:
        q.popleft()
```

- **What it does:**
    - If the new element is negative, it gets added to the back of our chronological queue.
    - If the element falling out of the window is negative, it *must* be the oldest negative number we are currently tracking (which sits at the front of the queue). Thus, `popleft()` safely and correctly discards it.

## Step 4: Recording the Result

Python

```python
    ans.append(q[0] if q else 0)

return ans
```

- **What it does:** Safely checks the front of the queue to grab the active "first negative" for the newly shifted window, appends it, and repeats until the array is fully processed.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find the first negative integer in a sliding window, maintain a FIFO queue that stores only the negative numbers. As the window slides, enqueue incoming negative numbers. If the outgoing number is negative, dequeue it from the front. The front of the queue always holds the target integer.
- **Data Structure Choice:** Double-ended Queue (`collections.deque`).
- **Algorithm Pattern:** Fixed-Size Sliding Window.
- **Complexity:**
    - **Time:** O(N)
    - **Space:** O(K)
- **Articulate the Solution:** "To optimally find the first negative integer in every window, I used a sliding window combined with a `deque`. I populated the deque with only the negative numbers from the first window. Then, as I slid the window across the array, I appended any incoming negative number to the queue. If the outgoing number was negative, I popped from the left of the queue. This guaranteed that the front of the deque always represented the first negative integer in the current window, achieving O(N) time complexity."

# Key Notes

- **Storing Values vs. Storing Indices:** Your approach of storing the raw *values* in the deque works perfectly for this specific problem because you only check `if outgoing < 0`. However, in more advanced deque problems, duplicate values can cause edge-case collisions if you aren't careful.
    - *The Standard Idiom:* It is often safer to store the **index** of the element in the deque, rather than the value itself.
    - *How it looks:* You append `i` instead of `arr[i]`. To clean the queue, you do `if q[0] <= i - k: q.popleft()`. This instantly proves if the element has fallen outside the window boundaries, regardless of its value!