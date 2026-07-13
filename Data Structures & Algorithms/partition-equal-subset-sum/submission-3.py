class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half_sum = total // 2
        false_paths = set()

        def backtrack(i, curr_sum):
            # Solution
            if curr_sum == half_sum:
                return True
            # Not a solution
            if i == len(nums) or curr_sum > half_sum:
                return False
            # If this combination cannot yield a result, exit
            if (i, curr_sum) in false_paths:
                return False
            # Try including and excluding num at i
            if backtrack(i + 1, curr_sum + nums[i]) or backtrack(i + 1, curr_sum):
                return True
            # This i and curr_sum cannot yield a result
            false_paths.add((i, curr_sum))
            return False

        return backtrack(0, 0)

# 1 2 3 | 6 -> True

# 1 3 | 6 | 2 -> True

# if the sum is odd then -> False

# if the sum is even AND ?

# 4 6 8 is even but there aren't two subsets of size 9

# try to create subsets of size sum/2?

# keep adding to one subset until you can't anymore then add to the other

# 1+2+3 , 6 = True
# 0,0 -> 1,0 -> 4,0 -> 4,6 -> 6,6

# 1 1 2 3 5
# this won't work because 1 needs to be paired with 5
# Can't add to just the smaller one either

# brute force?
# try every single partition = 2^n
#     if the curr_sum == sum/2 then we return True
#     once it passes curr_sum we can backtrack
