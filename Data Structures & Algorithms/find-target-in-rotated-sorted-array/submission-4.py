class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #left is sorted
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: #right is sorted
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1


# - r is the max of the right side
# - l is the min of the left side

# if target is < r
#     search right
# else 
#     search left

