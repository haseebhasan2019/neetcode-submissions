class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sets = []
        opens = 0
        curr = []

        def backtrack(i):
            if i == n*2:
                sets.append("".join(curr))
                return
            nonlocal opens
            if opens < n:
                opens+=1
                curr.append('(')
                backtrack(i+1)
                curr.pop()
                opens-=1
            closes = len(curr) - opens
            if opens > closes:
                curr.append(')')
                backtrack(i+1)
                curr.pop()

        backtrack(0)
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
