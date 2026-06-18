class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        l = 1
        r = max(piles)
        while l < r:
            k = (l+r) // 2
            hours = num_hours(k)
            if hours <= h:
                r = k
            else:
                l = k+1
        return l