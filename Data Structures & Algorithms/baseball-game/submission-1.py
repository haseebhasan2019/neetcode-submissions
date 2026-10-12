class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        total = 0
        for op in operations:
            if op == '+':
                stk.append(stk[-1] + stk[-2])
                total += stk[-1]
            elif op == 'D':
                stk.append(stk[-1] * 2)
                total += stk[-1]
            elif op == 'C':
                total -= stk.pop()
            else:
                stk.append(int(op))
                total += stk[-1]
        return total
'''
["1","2","+","C","5","D"]

1 2 5 10

'''