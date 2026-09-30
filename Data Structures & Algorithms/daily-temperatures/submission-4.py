class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
  
        for r in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[r]:
                l, lTemp = stack.pop()
                res[l] = r - l
            stack.append((r, temperatures[r]))
        return res
           
