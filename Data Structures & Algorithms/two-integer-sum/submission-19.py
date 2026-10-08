class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num -> i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return[seen[diff], i]
            seen[num] = i
        return [0,0]
