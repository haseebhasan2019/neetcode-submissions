class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        min_len = float('inf')
        while l <= r < len(nums):
            total += nums[r]
            if total >= target:
                # try to shorten window
                while total - nums[l] >= target:
                    total -= nums[l]
                    l+=1
                min_len = min(min_len, r-l+1)
            # Maintain window size - what about subtracting total
            if min_len != float('inf'):
                total -= nums[l]
                l+=1
            r+=1
        return 0 if min_len == float('inf') else min_len

'''
keep expanding the window until we get the first valid
then keep the window at that size and keep trying to shorten it
'''

