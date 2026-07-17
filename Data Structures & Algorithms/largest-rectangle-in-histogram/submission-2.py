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