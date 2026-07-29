from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
                
        # Can we cache the max coins for a sub problem?
        # Returns max coins
        @lru_cache(None)
        def rec(l, r) -> int:
            if l > r:
                return 0
            max_coins = 0
            for i in range(l, r+1):
                new_coins = nums[l-1] * nums[i] * nums[r+1]
                res_coins = rec(l, i-1) + new_coins + rec(i+1, r)
                max_coins = max(max_coins, res_coins)
            return max_coins

        return rec(1, len(nums)-2)

# arr = [4,2,3,7]
# rec(arr)
#     for each index in the range, split and get the max coins
#     4 = 1*4*2 + rec([2,3,7])
#         2 = 1*2*3 + rec([3,7])
#             3 = 1*3*7 + rec[7]
#                 7 = 7 === 8+6+21+7=42
#             7 = 3*7*1 + rec[3]
#                 3 = 3 === 8+6+21+3=38
#         3 = 2*3*7 + rec([2,7])
#             2 = 1*2*7 + rec([7])
#                 7 = 7 === 8+42+14+7=81
#     2 = 1*4*2 + rec([4,3,7])