class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix maximum - max up to this point
        # suffix maximum - ^ same but backwards
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        
        curr_max = height[0]
        for i in range(1, len(height)):
            prefix_max[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        curr_max = height[-1]
        for i in range(len(height)-2,-1,-1):
            suffix_max[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        water = 0
        for i in range(len(height)):
            water += max(0, min(prefix_max[i], suffix_max[i])-height[i])
        
        return water
        

# 3 1 3 = 2 = (x1 - x0 - 1) * min(y0, y1)
# 2 1 3 = 1 
# 3 1 0 1 -> 1
#   3 1 0 1 3 -> 1 + (min(y0, y1) - 1) * (x1-x0-1)
# p 0 3 3 3 3
# s 3 3 3 3 0

# first pointer must start at a non-zero height
# second pointer will be the next non-zero height

# 0 2 0 3 -> area = 2
#   f   s
# 0 2 3 4 -> 
#   f s

# 3 2 1 0 3 -> 6
# f       s

# water at each position = 
#     min(max left with a greater height, ...right...) - height

# There has to be a distance of at least 2 for there to be any
# rain water trapped