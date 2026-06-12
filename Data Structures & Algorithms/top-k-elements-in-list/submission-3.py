import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        d = Counter(nums)
        for key, val in d.items():
            heapq.heappush(minheap, (val,key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for val, key in minheap:
            res.append(key)
        return res