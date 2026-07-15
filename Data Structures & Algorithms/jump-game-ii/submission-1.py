class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        curr_end = 0
        jumps = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i >= curr_end:
                curr_end = max_reach
                jumps+=1
        return jumps

# [2,1,2,1,0]
# i = 0
# max_reach = 2
# curr_end = 2
# jumps = 1

# i = 1
# max_reach = 2
# curr_end = 2
# jumps = 1

# i = 2
# max_reach = 4
# curr_end = 4
# jumps = 2

# i = 3
# max_reach = 4
# curr_end = 4
# jumps = 2

# i = 4
# max_reach = 4
# curr_end = 4
# jumps = 2

# [2,4,1,1,1,1]
# i = 0
# max_reach = 0 -> 2
# curr_end = 0
# jumps = 0

# i = 1
# max_reach = 2 -> 5
# curr_end = 0 -> 5
# jumps = 0 -> 1

# i = 2
# max_reach = 5
# curr_end = 5
# jumps = 1

# i = 3
# max_reach = 5
# curr_end = 5
# jumps = 1

# i = 4
# max_reach = 5
# curr_end = 5
# jumps = 1

# i = 5
# max_reach = 5
# curr_end = 5
# jumps = 1


# [2,4,1] -> 1
#  0 1

# i = 0
# max_reach = 0 -> 2
# curr_end = 0
# jumps = 0

# i = 1
# max_reach = 2 -> 5
# curr_end = 0 -> 5
# jumps = 0 -> 1

# i = 2
# max_reach = 2 -> 5
# curr_end = 0 -> 5
# jumps = 0 -> 1