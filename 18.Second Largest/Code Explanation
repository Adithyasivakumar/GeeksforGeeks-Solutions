# Problem Explanation

## 18. Second Largest

## Step 1: Understand the Problem

- **Input:** An array of integers `arr`.
- **Output:** An integer representing the second strictly largest unique element in the array. If no such element exists (e.g., all elements are the same), return `1`.
- **Definition:** You need to find the element that is strictly smaller than the maximum element, but larger than all other elements.
- **Goal:** Traverse the array and dynamically keep track of the highest numbers seen so far without sorting the array, aiming for a single-pass O(N) solution.

## Step 2: Work Through Examples

- **Example 1:**
    - `arr` = `[12, 35, 1, 10, 34, 1]`
    - Read 12: `first` = 12.
    - Read 35: 35 > 12. `second` = 12, `first` = 35.
    - Read 1: Ignored (smaller than `second`).
    - Read 34: 34 > 12 but < 35. `second` = 34.
    - **Output:** `34`
- **Example 2:**
    - `arr` = `[10, 10, 10]`
    - Read 10: `first` = 10.
    - Next 10s are duplicates and get ignored. `second` never updates.
    - **Output:** `1`

## Step 3: Identify the Problem Type

- **Array Traversal:** Reading through elements one by one.
- **Top-K Tracking:** A classic pattern where you maintain a fixed number of variables to track the "top" values (in this case, Gold, Silver, and Bronze).

## Step 4: Think About Approaches

- **Sorting (O(NlogN) Time, O(1) Space):** Sort the array in descending order and iterate until you find a number strictly less than the first element.
    - *Critique:* Sorting does unnecessary work by organizing the entire array just to find one specific placement.
- **Two-Pass Scan (O(N) Time, O(1) Space):** Loop once to find the absolute maximum. Loop a second time to find the largest number that is strictly less than the absolute maximum.
    - *Critique:* Efficient and easy to read, but requires walking through the data twice.
- **Single-Pass Variable Tracking (O(N) Time, O(1) Space):** This is your provided code.
    - Maintain variables for the highest values seen.
    - Update them cascadingly as new high values come in.
    - *Critique:* This is the optimal, one-pass solution.

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```
function getSecondLargest(arr):
// 1. Initialize trackers to negative infinity
first = -infinity
second = -infinity

// 2. Scan every number
for num in arr:

    // 3. Skip if we've already tracked this exact number
    if num == first or num == second:
        continue

    // 4. If it's a new all-time high, shift everything down
    if num > first:
        second = first
        first = num

    // 5. If it's not the highest, but beats the silver medal
    else if num > second:
        second = num

// 6. Return -1 if no second largest was found
if second == -infinity: return -1
return second
```

## Step 6: Consider Edge Cases

- **Arrays with Duplicate Maximums:** `[5, 5, 4]`. The duplicate `5` is caught by the `continue` statement, allowing `4` to correctly take the `second` slot. Correct.
- **Arrays with Only One Unique Value:** `[2, 2]`. `first` becomes 2. `second` stays `inf`. At the end, the code returns `1`. Correct.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N), where N is the number of elements in the array. You iterate through the array exactly once, performing constant O(1) comparisons at each step.
- **Space Complexity:** O(1) auxiliary space. You only use a few tracking variables, requiring no extra memory regardless of the array's size.

## Step 8: Review and Reflect

- **Unnecessary Tracking:** Your code expertly tracks the first, second, *and third* largest numbers. While the cascading logic for `third` is flawlessly written, the problem only asks for the `second` largest. Removing the `third` variable entirely will make your code leaner and faster without changing the outcome!

# Code Explanation

## The Analogy: The Olympic Podium

Imagine an Olympic podium with three spots: Gold (`first`), Silver (`second`), and Bronze (`third`).
Initially, the podium is completely empty (`-math.inf`).
As athletes (numbers) finish their events, you check their scores.
If an athlete gets the exact same score as someone already on the podium, you tell them to go home (the `continue` check for duplicates).
If a new athlete breaks the world record (`num > first`), everyone has to shift down. The person in Silver drops to Bronze, the person in Gold drops to Silver, and the new athlete takes Gold.
If they don't break the world record, but they beat the Silver medalist (`num > second`), the Bronze medalist gets kicked off, Silver drops to Bronze, and the new athlete takes Silver.
After everyone has crossed the finish line, you just look at whoever is standing on the Silver podium!

## Step 1: Initializing the Podium

Python

```
import math
first = -math.inf
second = -math.inf
third = -math.inf
```

- **What it does:** Uses Python's `math.inf` to represent negative infinity. This guarantees that any valid integer in the array will be strictly larger than the initial baseline values.

## Step 2: Filtering Duplicates

Python

```
for num in arr:
    if num == first or num == second or num == third:
        continue
```

- **What it does:** Ensures we are looking for strictly *unique* largest values. If a number matches a value already standing on our podium, we skip to the next loop iteration immediately.

## Step 3: Cascading the Ranks

Python

```
    if num > first:
        third = second
        second = first
        first = num

    elif num > second:
        third = second
        second = num

    elif num > third:
        third = num
```

- **What it does:** This is the core logic.
    1. The first block triggers if `num` is a new absolute maximum. It safely transfers the current values down the chain *before* overwriting `first`, preventing data loss.
    2. The `elif` blocks ensure that a number is slotted into its correct respective tier without disturbing the values above it.

## Step 4: The Final Check

Python

```
if second == -math.inf:
    return -1
else:
    return second
```

- **What it does:** Evaluates the final state of the Silver tier. If it is still negative infinity, it means there weren't enough unique numbers in the array to fill the spot, returning the required `1`.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** Track the largest and second-largest elements in a single pass by dynamically cascading older values downward whenever a new higher value is encountered, ensuring duplicates are ignored.
- **Data Structure Choice:** Primitive Variables (In-Place Tracking).
- **Algorithm Pattern:** Single-Pass Top-K Tracking.
- **Complexity:**
    - **Time:** O(N).
    - **Space:** O(1).
- **Articulate the Solution:** "To find the second largest element optimally, I initialized tracking variables to negative infinity. I then iterated through the array in a single pass. For each element, I ignored it if it matched an already tracked value to ensure uniqueness. If the element was greater than my current maximum, I demoted the maximum to the second spot and updated the maximum. If it was only greater than the second maximum, I updated just the second spot. Finally, I returned the second tracking variable, or -1 if it remained at negative infinity."

## Spaced Repetition & Follow-ups:

- **LeetCode 414. Third Maximum Number:** This is the exact problem your code is actually written to solve! You should submit your code there, it will pass perfectly.
- **LeetCode 215. Kth Largest Element in an Array:** What happens when an interviewer asks for the 10th largest element? You can't hardcode 10 variables! (Hint: You will need to use a Min-Heap data structure).

# Key Notes

- **Leaner Implementation:** Since the problem strictly asks for the *second* largest, here is how you can streamline your exact logic to be perfectly tailored to the prompt, removing the `third` variable overhead:Python
    
    ```
    class Solution:
        def getSecondLargest(self, arr):
            first = float('-inf')
            second = float('-inf')
    
            for num in arr:
                if num > first:
                    second = first
                    first = num
                elif first > num > second:
                    second = num
    
            return second if second != float('-inf') else -1
    ```
    
    Notice how the condition `first > num > second` in the `elif` block inherently handles both the duplicate check and the size check in one clean, Pythonic line! Using `float('-inf')` also removes the need to `import math`.