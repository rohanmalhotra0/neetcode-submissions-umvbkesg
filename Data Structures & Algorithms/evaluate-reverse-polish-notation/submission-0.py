class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        currVals = deque()
        
        def sums(a,b):
            return a+b
        def products(a, b):
            return a*b
        
        for i in range(len(tokens)):
            if (tokens[i]).isnumeric():
                currVals.append(int(tokens[i]))
                
            elif tokens[i] == '+':
                # 1 , 2
                currVals.append(sum(currVals))
                while len(currVals) > 1:
                    currVals.popleft()
            elif tokens[i] == '-':
                currVals[1] *= -1
                currVals.append(sum(currVals))
                while len(currVals) > 1:
                    currVals.popleft()
            elif tokens[i] == '*':
                prod = products(currVals[0],currVals[1])
                currVals.append(prod)
                while len(currVals) > 1:
                    currVals.popleft()    
            elif tokens[i] == '/':
                div = currVals[0] / currVals[1]
                currVals.append(div)
                while len(currVals) > 1:
                    currVals.popleft()
        return currVals[0]            

