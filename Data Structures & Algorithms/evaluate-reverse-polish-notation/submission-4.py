from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currVals = deque()

        for i in range(len(tokens)):
            # Number, including negative numbers
            if tokens[i] not in "+-*/":
                currVals.append(int(tokens[i]))

            elif tokens[i] == '+':
                add = currVals[-2] + currVals[-1]
                currVals.pop()
                currVals.pop()
                currVals.append(add)

            elif tokens[i] == '-':
                sub = currVals[-2] - currVals[-1]
                currVals.pop()
                currVals.pop()
                currVals.append(sub)

            elif tokens[i] == '*':
                prod = currVals[-2] * currVals[-1]
                currVals.pop()
                currVals.pop()
                currVals.append(prod)

            elif tokens[i] == '/':
                div = int(currVals[-2] / currVals[-1])
                currVals.pop()
                currVals.pop()
                currVals.append(div)

        return currVals[0]