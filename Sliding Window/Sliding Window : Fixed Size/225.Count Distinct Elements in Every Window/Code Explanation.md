# Problem Explanation

## Count Distinct Elements in Every Window

## Step 1: Understand the Problem

- **Input:** An integer array `arr` and an integer `k`.
- **Output:** An array of integers where each element is the count of distinct numbers in each contiguous subarray (window) of size `k`.
- **Definition:** As you slide a window of size `k` across the array, elements enter the right side and leave the left side. You must track how many *unique* numbers currently exist inside the window.
- **Goal:** Avoid creating a brand new mathematical `set()` for every single window, which would waste compute time. Instead, dynamically track the frequencies of elements as they enter and exit.

## Step 2: Work Through Examples

- **Example 1:**
    - `arr` = `[1, 2, 1, 3, 4, 2, 3]`, `k = 4`
    - *Window 1:* `[1, 2, 1, 3]` $\rightarrow$ Frequencies: `{1: 2, 2: 1, 3: 1}`. Distinct count = `3`.
    - *Window 2:* Slide right. `1` leaves, `4` enters.
        - Current: `[2, 1, 3, 4]` $\rightarrow$ Frequencies: `{1: 1, 2: 1, 3: 1, 4: 1}`. Distinct count = `4`.
    - *Window 3:* Slide right. `2` leaves, `2` enters.
        - Current: `[1, 3, 4, 2]` $\rightarrow$ Frequencies: `{1: 1, 3: 1, 4: 1, 2: 1}`. Distinct count = `4`.
    - *Window 4:* Slide right. `1` leaves, `3` enters.
        - Current: `[3, 4, 2, 3]` $\rightarrow$ Frequencies: `{3: 2, 4: 1, 2: 1}`. (`1` was deleted!). Distinct count = `3`.
    - **Output:** `[3, 4, 4, 3]`

## Step 3: Identify the Problem Type

- **Sliding Window + Hash Map:** The sliding window tracks the physical boundaries of the subarray, while the Hash Map maintains the internal "state" (frequencies) of the elements currently inside those boundaries.

## Step 4: Think About Approaches

- **Brute Force with Sets ($O(N \times K)$ Time):** Loop through the array. For every index, take a slice `arr[i : i+k]`, cast it to a `set()`, and append its length to the answer array.
    - *Critique:* Too slow. Casting to a set forces the computer to iterate over all $K$ elements from scratch on every single step.
- **Sliding Window with Hash Map ($O(N)$ Time, $O(K)$ Space):** This is your provided code.
    - Use a dictionary to map `element -> frequency`.
    - Add the incoming element to the map, and subtract the outgoing element. If an outgoing element's frequency drops to 0, completely delete its key.
    - The number of distinct elements is always just `len(freq)`.
    - *Critique:* The optimal, industry-standard solution!

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```python
function countDistinct(arr, k):
// 1. Edge Case
if length of arr < k: return -1

// 2. Setup first window
freq = empty hash map
ans = empty array
for first k elements:
    increment their count in freq
append size of freq to ans

// 3. Slide the window
l = 0, r = k
while r < length of arr:
    // Add incoming
    increment count of arr[r] in freq

    // Remove outgoing
    decrement count of arr[l] in freq
    if count of arr[l] == 0:
        delete arr[l] from freq

    // Record current state
    append size of freq to ans
    l += 1, r += 1

return ans
```

## Step 6: Consider Edge Cases

- **Duplicates Entirely Fill the Window:** `arr = [1, 1, 1, 1], k = 2`. The map tracks `{1: 2}`. Distinct count is `1`. Perfect.
- **Out of Bounds Guard:** Your `if len(arr) < k: return -1` safely traps inputs where a window can't even be formed.

## Step 7: Complexity Analysis

- **Time Complexity:** $O(N)$. Populating the initial dictionary takes $O(K)$ time. The `while` loop runs $N - K$ times. Inside the loop, looking up, adding, and deleting from a Hash Map all take strictly $O(1)$ constant time. Thus, the total time is linear.
- **Space Complexity:** $O(K)$ auxiliary space. The `freq` hash map will never hold more than $K$ key-value pairs at any given moment. The output array `ans` takes $O(N - K + 1)$ space to store the results.

## Step 8: Review and Reflect

- **The Power of `del`:** The most critical line of your logic is `if freq[arr[l]] == 0: del freq[arr[l]]`. If you simply let the value stay at `0`, `len(freq)` would count the key as a valid distinct element, breaking the entire algorithm. You nailed the mechanics of Python dictionaries here!

# Code Explanation

## The Analogy: The Tour Bus

Imagine a tour bus that holds exactly `k` people. Every time the bus stops, the person sitting at the very back of the bus steps off (`arr[l]`), and a new person boards at the very front (`arr[r]`).

The tour guide keeps a clipboard with a tally of the *last names* of everyone currently on the bus (`freq`).

When a new person boards, the guide adds a tally mark next to their last name. When a person gets off, the guide erases a tally mark.

If a last name has zero tally marks left, the guide completely crosses that name off the clipboard (`del`).

Before driving to the next stop, the guide counts how many un-crossed names are on the clipboard (`len(freq)`) and writes that number in their official logbook (`ans`).

## Step 1: Initializing the First Window

Python

```
if len(arr) < k:
    return -1

freq = {}
ans = []

for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

ans.append(len(freq))
```

- **What it does:** Builds the initial state. It iterates through the first `k` elements, using `.get(arr[i], 0) + 1` to safely initialize or increment the frequency of each element. It then records the number of distinct keys as the answer for the first window.

## Step 2: Sliding the Pointers

Python

```
l, r = 0, k

while r < len(arr):
    freq[arr[r]] = freq.get(arr[r], 0) + 1
    freq[arr[l]] -= 1
```

- **What it does:** Establishes the left (`l`, outgoing) and right (`r`, incoming) boundaries. It adds the incoming element to the frequency map and subtracts the outgoing element.

## Step 3: Map Cleanup and Recording

Python

```
    if freq[arr[l]] == 0:
        del freq[arr[l]]

    ans.append(len(freq))

    l += 1
    r += 1
```

- **What it does:** This is the cleanup phase. If subtracting the outgoing element drops its count to 0, it is no longer present in the physical window, so its key is entirely removed from the Hash Map. It then measures the map's size to get the true distinct count, appends it to the results, and shifts both pointers forward for the next loop.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find distinct elements in a moving window, use a Hash Map to track frequencies. When sliding the window, increment the incoming element's frequency and decrement the outgoing element's frequency. Crucially, delete any key that hits a frequency of `0` so the size of the Hash Map always reflects the exact number of unique elements.
- **Data Structure Choice:** Hash Map + Array.
- **Algorithm Pattern:** Fixed-Size Sliding Window.
- **Complexity:**
    - **Time:** $O(N)$
    - **Space:** $O(K)$
- **Articulate the Solution:** "To efficiently count distinct elements in every window, I combined a sliding window with a Hash Map. I first initialized the frequency map for the initial window of size `K`. Then, using two pointers to slide the window, I updated the map in $O(1)$ time by incrementing the incoming element and decrementing the outgoing element. I explicitly deleted any outgoing element whose frequency reached zero to maintain an accurate dictionary length. By appending `len(freq)` at each step, I achieved an $O(N)$ time and $O(K)$ space solution."

# Key Notes

- **Simplifying the Pointers:** Your use of the explicit `while r < len(arr)` loop with `l` and `r` pointers is excellent and very easy to read. However, notice how `r` is just the current step of the loop, and `l` is exactly `r - k`.Python
    
    You can write this exact logic using the `for i in range(k, len(arr)):` structure you used in the previous "Max Sum Subarray" problem, saving a few lines of code and removing the need to manually increment pointers!
    
    ```python
    # An alternative loop structure without manual 'l' and 'r' variables
    for i in range(k, len(arr)):
        incoming = arr[i]
        outgoing = arr[i - k]
    
        freq[incoming] = freq.get(incoming, 0) + 1
        freq[outgoing] -= 1
    
        if freq[outgoing] == 0:
            del freq[outgoing]
    
        ans.append(len(freq))
    ```