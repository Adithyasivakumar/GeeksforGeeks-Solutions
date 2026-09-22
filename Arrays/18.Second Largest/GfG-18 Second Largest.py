import math
class Solution:
    def getSecondLargest(self, arr):
        
        first = -math.inf
        second = -math.inf
        third = -math.inf
        
        for num in arr:
        
            if num == first or num == second or num == third:
                continue
            
            if num > first:
                third = second
                second = first
                first = num
                
            elif num > second:
                third = second
                second = num
                
            elif num > third:
                third = num
            
        if second == -math.inf:
            return -1
        else:
            return second