from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        LIS.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                idx = bisect_left(LIS, nums[i])
                LIS[idx] = nums[i]
        return len(LIS)

'''
nlogn solution
- create longest increasing subsequence
- if num can be added to the end of the ss, add it
- else: find the insertion point in the LIS and replace it

[9,1,4,2,3,3,7]
9
1
1 4
1 2
1 2 3
1 2 3
1 2 3 7
'''