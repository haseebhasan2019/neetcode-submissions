class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = deque()
        operators = set(['+','-','*','/'])
        for token in tokens:
            if token in operators:
                num2 = stk.pop()
                num1 = stk.pop()
                if token == '+': stk.append(num1+num2)
                elif token == '-': stk.append(num1-num2)
                elif token == '*': stk.append(num1*num2)
                else: stk.append(int(num1/num2))
                print(stk[-1])
            else:
                stk.append(int(token))
        return stk.pop()

# 4 - (3 * (1+2)) = -5
# 4 3 1 2 + * -

# stk = -5

# when you reach an operand, pop twice, push the result of the operation
# - first pop = second num
# - second pop = first num
# when done iterating through list, result will be the only thing left on the stack

["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
22