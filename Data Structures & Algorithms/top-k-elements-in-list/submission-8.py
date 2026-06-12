class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_array = [[] for i in range(len(nums)+2)]
        freq_map = Counter(nums)
        for num, freq in freq_map.items():
            freq_array[freq].append(num)
        top_k_frequent = []
        for i in range(len(freq_array) -1, -1, -1):
            top_k_frequent += freq_array[i]
            if len(top_k_frequent) == k:
                break
        return top_k_frequent


# Bucket sort - index is frequency, value is nums of that frequency
# [  {}, {2}, {1} ]
# 0 - should be empty
# 1 - 2 has frequency 1
# 2 - 1 has frequency 2
# Max frequency will be the length of nums O(n)