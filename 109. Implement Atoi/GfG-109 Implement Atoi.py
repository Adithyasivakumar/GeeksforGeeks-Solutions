class Solution:
    def myAtoi(self, s):
        
        s = s.strip() # Removing leading and trailing whitespaces
        
        if not s: # If the string is empty, we'll return 0
            return 0
            
        sign = 1 # Sign tracker
        
        result = 0 # Where we will store our result
        
        if s[0] == "+" or s[0] == "-": # Sign assignment
            
            if s[0] == "-":
                sign = -1
            
            s = s[1:] # Starting from next element
        
        for char in s:
            
            if not char.isdigit(): # If not digit
                break
            
            result = result * 10 + int(char) # Makes room for new digits
        
        result = result * sign # Assigning the sign
        
        #Constraints   
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
            
        elif result < -2 ** 31:
            return -2 ** 31
            
        else:
            return result