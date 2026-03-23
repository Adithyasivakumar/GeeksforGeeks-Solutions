#Iterative Approach
#Faster

class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return 1
        
        result = 1
        
        for i in range(2, n + 1):
            result = result * i
        
        return result

    
#Recursive Approach
#Slower

class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        
        if n == 1:
            
            return 1
            
        return n * self.factorial(n - 1)