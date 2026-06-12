class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_array = [set() for i in range(len(nums)+2)] # Need the max frequency to be nums+1
        freq_map = Counter(nums) # produces frequency of every number in nums
        # 1 1 2 4
        # 1: 2, 2: 1, 4: 1 (num: frequency)
        for num, freq in freq_map.items():
            freq_array[freq].add(num)
        print(freq_array)
        top_k_frequent = []
        # iterate backwards from the end of freq_array and start adding to output until reach k
        for i in range(len(freq_array) -1, -1, -1):
            top_k_frequent += list(freq_array[i])
            if len(top_k_frequent) == k:
                break
        return top_k_frequent


# Bucket sort - index is frequency, value is nums of that frequency
# [  {}, {2}, {1} ]
# 0 - should be empty
# 1 - 2 has frequency 1
# 2 - 1 has frequency 2
# Max frequency will be the length of nums O(n)