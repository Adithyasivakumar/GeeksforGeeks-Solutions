#User function Template for python3

class Solution:
    def rotate(self, arr):
        
        k = 1
        
        n = len(arr)
        
        k = k % n
        
        rotated_array = arr[-k:] + arr[:-k]
        
        arr[:] = rotated_array
        
        return arr