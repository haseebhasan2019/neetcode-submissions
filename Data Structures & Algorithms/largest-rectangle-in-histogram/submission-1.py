class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        for i, height in enumerate(heights):
            start_idx = i
            while stack and height <= stack[-1][1]:
                top_idx, top_height = stack.pop()
                area = (i-top_idx) * top_height
                max_area = max(max_area, area)
                start_idx = top_idx
            stack.append((start_idx, height))
        while stack:
            start_idx, height = stack.pop()
            area = (len(heights)-start_idx) * height
            max_area = max(max_area, area)
        return max_area
# [2,1,5,6,2,3]
# stack = (0,1) (2,5) (3,6)
# max_area = 2

# [7,1,7,2,2,4]
# stack = [(0,7) ]
# -> [(0,1)]
# -> [(0,1) (2,2)]
# -> [(0,1) (2,2) (5,4)]
# -> [(0,1) (2,2)]
# -> [(0,1)]
# -> []
# max_area = 2 -> 4 -> 6 4? -> 8 6?
# return 6


# [1,3,7]
# stack = [(0,1) (1,3) (2,7)]
# max_area = 7 3? 1?

# 1 2 3 4 2 2
# stack = [(0,1) (1, 2) (2,3) (3,4)] 
# -> [(0,1) (1, 2) (2,3)]
# -> [(0,1) (1, 2)]
# -> [(0,1) (1, 2)]
# max_area = 4 -> 6 -> 8

# 1 3 5 2 2
