class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = water = 0
        while l < r:
            if height[r] > height[l]:
                water += max(0, min(left_max, height[r]) - height[l])
                left_max = max(left_max, height[l])
                l+=1
            else: # left height is greater than or equal to right height
                water += max(0, min(height[l], right_max) - height[r])
                right_max = max(right_max, height[r])
                r-=1
        return water
#  2 0 1
# when height[r] > height[l] -> add water of l, advance l, maxSoFar updated