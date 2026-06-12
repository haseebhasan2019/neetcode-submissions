class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float('inf')
        while l <= r:
            m = (l+r) // 2
            local_min = min(nums[l], nums[m], nums[r])
            minimum = min(minimum, local_min)
            if nums[l] == minimum or nums[r] == minimum:
                l = m+1
            else:
                r = m-1
        return minimum

# need to go left of min(l,m,r)

# if left is the min(l,m,r) -> return l
# if right is the smallest -> search right
# else: 

# 1 2 3 4
# 6 7 1 2 3 4 5

# 10... 20 ...5

# 6 1 2 3 4 5
# 1 2 3 4 5 6


# if left < mid -> left side is sorted
#     if target < mid and >= left -> go left
#     else go right
# if right > mid -> right side is sorted:
#     if target is in the right side range go right else go left