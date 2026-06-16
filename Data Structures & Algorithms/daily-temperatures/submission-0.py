class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = deque()
        res = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stk and num > temperatures[stk[-1]]:
                top_idx = stk.pop()
                res[top_idx] = i-top_idx # num days we need to wait                
            stk.append(i)
        return res

# temps = [30,38,30,36,35,40,28]
# res = [1,4,1,2,1,0,0]
# stk = []

# ***bug = multiple vals < num***

# temps = [22,21,20]
# res = [0, 0, 0]
# stk = [0,1,2] - indexes that are waiting for higher temperatures to come
# top_idx = 

# [30,28,30,36] -> [3, 1, 1, 0]
# [20, 22, 24] -> [1,1,0]
# [20 18 22 20 24] -> [2 1 2 1 0]

# maybe i goes on the stack

# [20, 22, 24] -> [1,1,0]
# [0, 0, 0]
# res (days waiting) = i - stack.pop() (index in stack)
# stack [1]
#          0.  1.  2.  
# temps = [20, 18, 22]
# res = [2, 1, 0] (always fill in last index with 0)

# stack = [0, 1]


# temps = [23 18 22 20 24]
# res = [0, 2]
# stack will always be in decreasing order
# * saving each index for a future value that's greater than that index
# For anything left on the stack set that index to 0

# temps = [7,6,5]

# stk = [0, 1, 2]