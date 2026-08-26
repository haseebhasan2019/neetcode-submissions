class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, f in freq.items():
            heapq.heappush(heap, (f,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for _, key in heap]
        
# want the k most frequent elements
    
# 5 3 4 2 4 4 2

# 2: 2
# 3: 1
# 4: 3
# 5: 1

# k = 1 -> 4
# k = 2 -> [4,2]


# heap of size k

# if the frequency is greater than the lowest frequency in the heap, pop and push
