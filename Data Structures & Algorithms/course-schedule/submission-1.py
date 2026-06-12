class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        visited = set()

        def hasCycle(course, visiting):
            if course in visiting:
                return True
            if course in visited:
                return False
            visiting.add(course)
            for prereq in prereqs[course]:
                if hasCycle(prereq, visiting):
                    return True
            visiting.remove(course)
            visited.add(course)
            return False
        
        for course in range(numCourses):
            if hasCycle(course, set()):
                return False
        return True