class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        for key, freq in freq_map.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        k_frequent_list = [key for freq, key in heap]
        return k_frequent_list

# 1. minheap of size k
# 2. bucketsort