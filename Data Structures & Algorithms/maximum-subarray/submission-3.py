class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, 0)
            max_sum = max(max_sum, curr_sum)
        return max_sum if max_sum else max(nums)


'''
Input: nums = [2,-3,4,-2,2,1,-1,4]
max = 2
if adding the number to the running sum makes it negative, reset running sum
otherwise, add it along, update max_subarray and curr_subarray


-1 -2 -3 0 -> 0

-1 -2 -3 -> -1 NOT 0
'''