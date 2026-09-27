# Standard Approach

class Solution:
    def countDistinct(self, arr, k):
        
        if len(arr) < k:
            return -1
            
        freq = {}
        
        ans = []
        
        for i in range(k):
            
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            
        ans.append(len(freq))
        
        for i in range(k, len(arr)):
            
            incoming = arr[i]
            outgoing = arr[i - k]
            
            freq[incoming] = freq.get(incoming, 0) + 1
            
            freq[outgoing] -= 1
            
            if freq[outgoing] == 0:
                del freq[outgoing]
                
            ans.append(len(freq))
            
        return ans