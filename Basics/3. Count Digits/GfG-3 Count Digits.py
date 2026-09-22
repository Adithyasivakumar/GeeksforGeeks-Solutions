#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        
        original_n = n
        string_n = str(n)
        
        count = 0
        
        for digit_char in string_n:
            
            digit = int(digit_char)
            
            if digit != 0 and original_n % digit == 0:
                count += 1
                
        return count