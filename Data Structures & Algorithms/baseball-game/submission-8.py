class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] is True:
                stack.append(int(operations[i]))
            if operations[i] == "+" and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            if operations[i] == "C" and len(stack) >= 1:
                stack.pop()
            if operations[i] == "D":
                stack.append(2 * stack[-1])
        return sum(stack)