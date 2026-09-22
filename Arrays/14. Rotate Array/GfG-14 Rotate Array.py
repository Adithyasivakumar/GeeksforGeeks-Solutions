#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        
        n = len(arr)
        d = d % n
        
        if d == 0:
            return arr
            
        relocated_part = arr[d:] + arr[:d]
        
        arr[:] = relocated_part