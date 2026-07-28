class Solution:
    def checkValidString(self, s: str) -> bool:
        min_opens = 0
        max_opens = 0
        for c in s:
            if c == '(':
                min_opens += 1
                max_opens += 1
            elif c == ')':
                min_opens -= 1
                max_opens -= 1
            else:
                min_opens -= 1
                max_opens += 1
            min_opens = max(min_opens, 0)
            if max_opens < 0:
                return False
        return min_opens == 0

"""
maintain min_opens to ensure no leftover opens by the end
maintain max_opens to ensure there are no closes without opens
"""