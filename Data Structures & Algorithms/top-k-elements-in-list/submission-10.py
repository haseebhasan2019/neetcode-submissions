class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency map of each number
        # Convert that into a list of tuples (-freq, num)
        # heapify the list
        # Return top k
        # O(m) where m is the amount of unique numbers
        # if you don't heapify and insert one by one: O(mlogm)
        counter = Counter(nums)
        heap = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res
