#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        
        if b == "0":
            return 1
        
        last_a = int(a[-1])
        
        if last_a == "0":
            return 0
        
        exp = 0
        
        for digit in b:
            
            exp = (exp * 10 + int(digit)) % 4
            
            if exp == 0:
                exp = 4
            
        return pow(last_a , exp, 10)