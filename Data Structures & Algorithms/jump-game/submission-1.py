class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        jumps = deque()
        jumps.append(0)
        visited = set()
        while jumps:
            i = jumps.pop()
            visited.add(i)
            max_jump = nums[i]
            for jump in range(1, max_jump+1):
                new_i = i+jump
                if new_i == len(nums)-1:
                    return True
                elif new_i < len(nums)-1:
                    if new_i not in visited:
                        jumps.append(new_i)
                else:
                    break
        return False