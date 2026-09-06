class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:

            # Step 1: Number -> add to stack
            if token not in "+-*/":
                stack.append(int(token))

            # Step 2: Operator -> get last two numbers
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)

                elif token == '-':
                    stack.append(a - b)

                elif token == '*':
                    stack.append(a * b)

                elif token == '/':
                    stack.append(int(a / b))

        return stack[0]