class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Single pass
        d = {}
        for i, n in enumerate(nums):
            if target - n in d and d[target - n] != i:
                return [d[target - n], i]
            d[n] = i