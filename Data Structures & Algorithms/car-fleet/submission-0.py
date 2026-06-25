class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = [(position[i], (target-position[i]) / speed[i]) for i in range(len(speed))]
        pos_time.sort()
        fleets = 1
        time_cap = pos_time[-1][1]
        for i in range(len(pos_time)-2,-1,-1): #iterate backwards
            t = pos_time[i][1]
            if t > time_cap:
                fleets+=1
                time_cap = t
        return fleets

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# pos_time = (0, 10), (1, 4.5),  (4, 3), (7, 3)

# can a starting position be after target? no


# p 1 4
# s 3 2
# target = 10

# pos_time = (1, 3), (4, 3)



# while time is greater than or equal to the prev time CAP num fleets same
# once time is less than prev time CAP, then a new fleet starts
# but this would require positions to be sorted


# p 5
# s 1
# target = 10
# he will reach target 

# fleets <= number of cars
# fleets = grouping of cars
# can cars be at the same position?

# starting position matters because a car cannot pass any car ahead of it
# when a car catches up to a car ahead of it, it is bound by its speed

# p 1 4
# s 3 2
# target = 10
# reaches: both cars reach 10 at 3hrs
# if car 2 had speed 1 then it would've reached in 6 hours
# if car 2 had speed 3 then it would've reached in 3 hours 
#     because it is bound by the car ahead 2 hrs is less than 3 hrs
