class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_area
# move the smaller height
# update maxArea


# 1 2 7 1 1 1 7 3 2
#     x       x
# area = 1*8 = 8
# 2*7 = 14
# 2*6 = 12
# 3*5 = 15
# 4*7 = 28