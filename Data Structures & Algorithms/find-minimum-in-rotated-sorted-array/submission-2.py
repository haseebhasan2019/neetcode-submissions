class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if len(nums)==1:
            return nums[0]
        minval = 1001

        while l <= r:
            if nums[r] > nums[l]:
                minval = min(minval, nums[l])
                break
            m = (l+r)//2
            minval = min(minval, nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return minval
# go left

# r < l < m 
# right



# 1 2 3 4 5
# left

# 2 3 4 5 1
# right

# 3 4 5 1 2
# right

# 4 5 1 2 3
# center

# 5 1 2 3 4
# left

# perform binary search on the left side then the right side for min
# p

# 6 7 8 1 2 3 4 5 


# 3 4 5 6 7 8 1 2 