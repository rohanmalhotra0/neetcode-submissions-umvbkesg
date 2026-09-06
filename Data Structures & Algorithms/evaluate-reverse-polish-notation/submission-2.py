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
                add = currVals[len(currVals) - 2] + currVals[len(currVals) - 1]
                currVals.pop()
                currVals.pop() 
                currVals.append(add)
                
            elif tokens[i] == '-':
                sub = currVals[len(currVals) - 2] - currVals[len(currVals) - 1]
                
                currVals.pop()
                currVals.pop() 
                currVals.append(sub)
                
            elif tokens[i] == '*':
                prod = currVals[len(currVals) - 2] * currVals[len(currVals) - 1]
                
                currVals.pop()
                currVals.pop()  
                currVals.append(prod)
            elif tokens[i] == '/':
                div = currVals[len(currVals) - 2] // currVals[len(currVals) - 1]
                
                currVals.pop()
                currVals.pop()
                currVals.append(div)
        return currVals[0]            

