class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sets = []
        curr = []

        def backtrack(opens, closes):
            if len(curr) == n*2:
                sets.append("".join(curr))
                return
            if opens < n:
                curr.append('(')
                backtrack(opens+1, closes)
                curr.pop()
            if opens > closes:
                curr.append(')')
                backtrack(opens, closes+1)
                curr.pop()

        backtrack(0, 0)
        return sets


# 1 = 
# ()
# 2 = 
# (())
# ()()
# 3 = 
# ((()))
# (()())
# (())()
# ()(())
# ()()()

# each stage you have a choice of open or close
# Can only choose a close bracket if there are more opens than closes
# keep track of current number of open parentheses
# Can only choose an open parenthesis if it is less than n
