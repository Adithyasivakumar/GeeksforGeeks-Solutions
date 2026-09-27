# Problem Explanation

## 224. Max Sum Subarray of size K

## Step 1: Understand the Problem

- **Input:** An array of integers `arr` and an integer `k`.
- **Output:** The maximum possible sum among all contiguous subarrays of exactly size `k`.
- **Definition:** A "subarray" is a contiguous slice of the original array. You need to look at every possible group of `k` numbers sitting next to each other and find the group with the highest total.
- **Goal:** Compute the maximum sum efficiently without repeatedly recalculating the sum of overlapping elements from scratch.

## Step 2: Work Through Examples

- **Example 1:**
    - `arr` = `[2, 1, 5, 1, 3, 2]`, `k = 3`
    - Window 1: `[2, 1, 5]` → Sum = 8
    - Window 2: `[1, 5, 1]` → Sum = 7
    - Window 3: `[5, 1, 3]` → Sum = 9
    - Window 4: `[1, 3, 2]` → Sum = 6
    - **Output:** `9` (from the subarray `[5, 1, 3]`)

## Step 3: Identify the Problem Type

- **Sliding Window (Fixed Size):** This is the quintessential introduction to the Sliding Window pattern. Whenever a problem asks for maximums, minimums, or averages of contiguous subarrays of a *fixed* length, a fixed sliding window is the optimal tool.

## Step 4: Think About Approaches

- **Brute Force (O(N×K) Time):** Run a `for` loop starting at every index, and run an inner loop to add up the next `k` elements.
    - *Critique:* If N is 100,000 and K is 50,000, this requires 5 billion operations. It recalculates the exact same overlapping numbers over and over again, causing a Time Limit Exceeded (TLE) error.
- **Sliding Window (O(N) Time, O(1) Space):** This is your provided code.
    - Calculate the sum of the very first window of size `k`.
    - To get the sum of the next window, take the current sum, subtract the element that is falling out of the left side of the window, and add the new element entering the right side of the window.
    - *Critique:* This is the universally accepted, mathematically optimal solution. It touches every element a maximum of two times.

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```
function maxSubarraySum(arr, k):
// 1. Edge Case
if length of arr < k: return -1

// 2. Setup initial window
current_window = sum of first k elements
max_window = current_window

// 3. Slide the window across the array
for i from k to end of arr:
    outgoing_element = arr[i - k]
    incoming_element = arr[i]

    current_window = current_window + incoming_element - outgoing_element
    max_window = maximum of (max_window, current_window)

return max_window
```

## Step 6: Consider Edge Cases

- **Array smaller than K:** If `arr = [1, 2]` and `k = 3`, you can't form a subarray of size 3. Your `if len(arr) < k: return -1` correctly traps this error in O(1) time.
- **Negative Numbers:** The logic holds perfectly even if the array contains negative numbers, because subtracting a negative outgoing element correctly *increases* the window sum (e.g., `(-5) = +5`).

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). Calculating the initial window sum takes O(K) time. The `for` loop runs exactly N−K times, performing O(1) arithmetic on each iteration. The total time is strictly linear.
- **Space Complexity:** O(1) auxiliary space. You only maintain two integer variables (`current_window` and `max_window`) regardless of how massive the input array is.

## Step 8: Review and Reflect

- **Mastery Established:** This code is pristine. The transition from O(N2) brute force array slicing to O(N) sliding window arithmetic is a major milestone in algorithmic optimization, and your execution here is flawless.

# Code Explanation

## The Analogy: The Picture Frame

Imagine a long line of numbered wooden blocks on a table. You have a rigid picture frame that is exactly wide enough to show `k` blocks at once.
You place the frame over the first `k` blocks and add up their values.
Now, you want to see the total of the *next* possible group. Instead of lifting the frame up and recounting all the blocks from scratch, you simply slide the frame exactly one block to the right.
When you do this, exactly **one block leaves the left side** of the frame, and exactly **one new block enters the right side**.
To get your new total, you just take your old total, subtract the number that left, and add the number that entered!

## Step 1: The Initial Frame

Python

```
if len(arr) < k:
    return -1

current_window = sum(arr[:k])
max_window = current_window
```

- **What it does:** Validates the input size. It then uses Python's highly optimized built-in `sum()` function to calculate the total of the first `k` elements (`arr[0]` to `arr[k-1]`), initializing both the running total and the maximum tracker.

## Step 2: Sliding the Frame

Python

```
for i in range(k, len(arr)):
```

- **What it does:** Starts the loop exactly where the first window left off (index `k`), and iterates to the end of the array. The index `i` represents the new element entering the right side of the window.

## Step 3: The O(1) Math Update

Python

```
    current_window = current_window + arr[i] - arr[i - k]
```

- **What it does:** This is the heart of the Sliding Window technique.
    - `arr[i]`: The new element sliding into the frame from the right.
    - `arr[i - k]`: The old element that is currently exactly `k` steps behind `i`, meaning it is the one being pushed out of the left side of the frame.
    - It updates the running total instantly without recalculating the overlap.

## Step 4: Tracking the Maximum

Python

```
    max_window = max(max_window, current_window)

return max_window
```

- **What it does:** Compares the freshly calculated window sum against the highest sum seen so far, storing the winner. Once the frame reaches the end of the array, it returns the absolute maximum found.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find the maximum contiguous sum of a fixed size, calculate the sum of the first window, then slide the window across the array. At each step, update the sum in O(1) time by adding the new incoming element and subtracting the old outgoing element.
- **Data Structure Choice:** Primitive variables (Accumulators).
- **Algorithm Pattern:** Fixed-Size Sliding Window.
- **Complexity:**
    - **Time:** O(N)
    - **Space:** O(1)
- **Articulate the Solution:** "To solve this optimally, I implemented a fixed-size sliding window. I first computed the sum of the initial window of size K. Then, I iterated through the remainder of the array, updating the window sum in O(1) time by subtracting the element that exited the window's left edge and adding the new element that entered its right edge. By keeping a running maximum of these sums, I found the largest subarray sum in strictly O(N) time and O(1) auxiliary space."

Now that you have mastered the Fixed Sliding Window, it's time to tackle the Dynamic Sliding Window (where the frame stretches and shrinks). Which of these classic dynamic window problems would you like to conquer next?

Minimum Size Subarray Sum

Longest Substring Without Repeats

# Key Notes

- **Floating Point Averages:** A very common variation of this problem is "Maximum Average Subarray I" (LeetCode 643). The logic is 100% identical. You just calculate the `max_window` sum exactly as you did here, and at the very end, `return max_window / k`.
- **String Anagrams:** The sliding window isn't just for adding numbers! If you are asked to find anagrams of a string `p` inside a massive string `s` (LeetCode 438), you can use this exact sliding window frame. Instead of tracking a `current_window` sum, you track a `current_window` Hash Map of character frequencies, adding the incoming character and deleting the outgoing one!