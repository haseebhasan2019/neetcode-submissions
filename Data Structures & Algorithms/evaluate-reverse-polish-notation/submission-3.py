class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }
        for token in tokens:
            if token in operators:
                b = stk.pop()
                a = stk.pop()
                stk.append(operators[token](a,b))
            else:
                stk.append(int(token))
        return stk.pop()