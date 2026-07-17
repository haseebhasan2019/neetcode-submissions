class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance_to_origin(point):
            return (point[0] ** 2 + point[1] ** 2) ** 0.5

        heap = [] # (distance, point) of size k
        for point in points:
            dist = distance_to_origin(point)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        # construct list of points without distances
        return [point for _, point in heap]

