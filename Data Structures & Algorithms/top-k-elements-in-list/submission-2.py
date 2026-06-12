from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = Counter(nums) # num -> freq
        counts = [[] for i in range(len(nums)+1)]
        for num, freq in freqList.items():
            counts[freq].append(num)
        res = []
        print(counts)
        counts.reverse()
        for l in counts:
            res.extend(l)
            if len(res) == k:
                return res
        