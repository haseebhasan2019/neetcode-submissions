from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = Counter(nums)
        heapItems = [(-freq, num) for num, freq in freqList.items()]
        heapq.heapify(heapItems)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heapItems)[1])
        return res
            

# Hashmap frequency list - Counter
# Push pairs onto a heap of size k