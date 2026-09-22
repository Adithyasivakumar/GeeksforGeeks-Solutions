# optimal solution

class Solution:
    def search(self, arr, x):
        # Loop through the array, getting the index 'i'.
        for i in range(len(arr)):
            # If we find a match...
            if arr[i] == x:
                # ...return the index immediately and stop.
                return i
        
        # If the loop finishes without finding x, return -1.
        return -1