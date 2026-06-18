class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def num_hours(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            hours = num_hours(k)
            if hours <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res