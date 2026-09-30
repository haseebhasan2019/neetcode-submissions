class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_i = 0
        for i in range(len(nums)):
            if i > last_i:
                return False
            last_i = max(last_i, i + nums[i])
        return True
'''
 0 1 2 3 4
[1,2,0,1,0]
last_i = 0
0 - last_i = 1
1 - last_i = 3
2 - last_i = 3
3 - last_i = 4
4 - last_i = 4
'''