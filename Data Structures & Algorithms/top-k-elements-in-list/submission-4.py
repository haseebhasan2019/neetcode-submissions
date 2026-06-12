from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        d = Counter(nums)
        for key, freq in d.items():
            heapq.heappush(minheap, (freq, key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        for freq, key in minheap:
            res.append(key)
        return res
