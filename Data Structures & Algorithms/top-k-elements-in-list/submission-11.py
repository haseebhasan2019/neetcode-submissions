class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep an array, index reperesents frequency
        # array: mapping of frequency -> [elements]
        # O(n) - hashmap + bucket array

        bucket = [[] for _ in range(len(nums)+1)]
        freq = Counter(nums) # element -> frequency
        for element, frequency in freq.items():
            bucket[frequency].append(element)
        res = []
        print(bucket)
        index = len(bucket) - 1
        while len(res) < k:
            res.extend(bucket[index])
            index-=1
        return res

# bucket: [ ,[1] ,[2] ,[3] , , , ]


# [5, 6, 6, 7, 7, 7]

# element -> freq
# 5: 1
# 6: 2
# 7: 3

# k = 2

# return 6,7

# minheap -> is of size k keep track of k largest elements, pop off anything higher than min
# keeping track of freqency tuple (freq, num)

# n = len of nums
# m = unique nums
# O(n + m*log(k))


# # new approach

# 5: 1
# 6: 2
# 7: 3

# keep an array, index reperesents frequency

# array: mapping of frequency -> [elements]
# O(n) - hashmap + bucket array
