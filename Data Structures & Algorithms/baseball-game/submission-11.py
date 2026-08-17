class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            if operations[i] == "C" and len(stack) >= 1:
                stack.pop()
            if operations[i] == "D" and len(stack) >= 1:
                stack.append(2 * stack[-1])
            else:
                stack.append(int(operations[i]))
        return sum(stack)