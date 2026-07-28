class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
                if high < 0:
                    return False
            else:
                low -= 1
                high += 1
            low = max(low, 0)
        return low == 0

# low/high are a range of how many unclosed ( could exist right now

# low = min possible opens - treat * as ) 
# high = max possible opens - treat * as ( 
# If high ever goes negative, too many ) 
# Clamp low at 0. At the end, valid iff low == 0

# (())
# (()()(()()))

# )()(
# ()())(

# if there are open parentheses, * should close?
# (((***))) ?

# ()()()**()**()))
# 2 unopened close parentheses at the end
# Since 2 stars came before those are valid
# wildcard decrements by two

# ((((****
# accumulated 4 wildcards
# and there are 4 open parentheses

# as you iterate through you maintain a stack
# push open parentheses onto the stack
# when theres a close parenthesis, pop from stack
# when theres a wildcard, increment counter

# if there is a close parenthesis but empty stack: wildcard--
# if there are leftover open parentheses after iterating through the string: 
#     check if it is less than or equal to wildcard counter

