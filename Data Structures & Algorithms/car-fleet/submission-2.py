class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0
        time_cap = None
        for pos, spd in cars:
            t = (target - pos) / spd
            if not time_cap or t > time_cap:
                fleets+=1
                time_cap = t
        return fleets

# starting position matters because a car cannot pass any car ahead of it
# when a car catches up to a car ahead of it, it is bound by its speed
# sort tuples of (position, time to target)
# while ttt is less than the time CAP, num fleets same (will be bound by longer time ahead)
# once time is greater than time CAP, then a new fleet starts (won't reach the ahead fleet)