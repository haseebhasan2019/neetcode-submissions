class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for val in nums:
            num = abs(val)
            if nums[num-1] < 0:
                return num
            nums[num-1] *= -1
        return -1

# Check each element from the array in a set, and when the num is already in the set, we have the dup - O(n) time+space

# 1+2+3+4+5=15
# -1,2,-3,2,2=10

# Use the input array as a hashset via index - mark with negative
# nums: n + 1
# vals: 1 - n
# index: 0 - n-1