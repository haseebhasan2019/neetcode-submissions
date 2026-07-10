class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_after = defaultdict(list)
        in_deg = [0] * numCourses
        visited = 0

        # map pre-reqs to their courses
        for course, prereq in prerequisites:
            courses_after[prereq].append(course)
            in_deg[course] += 1

        q = deque()
        # Find courses that have no prerequisites
        for course in range(len(in_deg)):
            if not in_deg[course]:
                q.append(course)
                visited +=1
        while q:
            course = q.popleft()
            for course_after in courses_after[course]:
                in_deg[course_after] -= 1
                if in_deg[course_after] == 0:
                    q.append(course_after)
                    visited +=1
        return visited == numCourses


        # 1 -> 2 -> 3

        # [2,1] [3,2]

        
        # prereq -> course
        # 1 - 2
        # 2 - 3

        # in_deg
        # 1 - 
        # 2 - 0
        # 3 - 0

        # queue up all classes that have no pre-reqs
        # then search the classes that have that class as a prereq and decrease the indegree by 1 