class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        output = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom_index = stack.pop()
                
                if not stack:
                    break
                    
                left_index = stack[-1]
                water_height = min(height[i], height[left_index]) - height[bottom_index]
                width = i - left_index - 1
                output += water_height * width
            
            stack.append(i)
        
        return output