class CountSquares:

    def __init__(self):
        self.store = defaultdict(int) # point -> count

    def add(self, point: List[int]) -> None:
        self.store[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        square_set = set()
        count = 0
        
        def same_axis(point1, point2):
            return point1[0] == point2[0] or point1[1] == point2[1]

        def same_point(point1, point2):
            return point1 == point2
        
        def get_both_sides(point1, point2):
            sides = []
            dist = abs((point1[0] - point2[0]) + (point1[1] - point2[1]))
            if point1[0] == point2[0]:
                sides.append([(point1[0] - dist, point1[1]),(point2[0] - dist, point2[1])])
                sides.append([(point1[0] + dist, point1[1]),(point2[0] + dist, point2[1])])
            else:
                sides.append([(point1[0], point1[1] - dist),(point2[0], point2[1] - dist)])
                sides.append([(point1[0], point1[1] + dist),(point2[0], point2[1] + dist)])
            return sides
        point = tuple(point)
        for point2 in self.store:
            if same_axis(point, point2) and not same_point(point, point2):
                for point3, point4 in get_both_sides(point, point2):
                    if tuple(point3) in self.store and tuple(point4) in self.store: 
                        # valid square
                        square = tuple(sorted([point, point2, point3, point4]))
                        if square not in square_set:
                            square_set.add(square)
                            count += self.store[point2] * self.store[point3] * self.store[point4]
        return count
        
# add - add new points to the stream, duplicates ok
# query - given point + iterate through each point in the storage + both sides of the line 
#      only choose points that are on the same x or y axis / not the same point
#     how to ensure there aren't duplicate solutions - sort solution 
#         duplicate to avoid - iterating through the same points that were already added as a solution
#         duplicate to include - the first solution - keep a count of the number of duplicates (solution count)
