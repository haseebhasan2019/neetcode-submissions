class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary of value to its index
        d = defaultdict(int)
        for i, n in enumerate(nums):
            d[n] = i
        for i, n in enumerate(nums):
            if target - n in d and d[target - n] != i:
                return [i, d[target - n]]