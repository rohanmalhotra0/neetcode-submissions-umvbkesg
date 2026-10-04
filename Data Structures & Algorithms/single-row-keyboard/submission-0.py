class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_indices = {}
        # Get the index for each key.
        for i in range(len(keyboard)):
            key_indices[keyboard[i]] = i
            
        
        prev = 0
        result = 0
        
        # Calculate the total time.
        for c in word:
          
            result += abs(prev - key_indices[c])
            
           
            prev = key_indices[c]
            
        return result