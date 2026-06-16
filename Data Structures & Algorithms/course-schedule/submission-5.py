class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_deg = [0] * numCourses # num of prereqs for course i
        graph = defaultdict(list) # course -> children
        for course, prereq in prerequisites:
            in_deg[course]+=1
            graph[prereq].append(course)
        # queue up classes with no prereqs
        queue = deque()
        visited = 0
        for course in range(numCourses):
            if in_deg[course] == 0:
                queue.append(course)
        # iterate through queue and decrease in-degs of children
        while queue:
            course = queue.popleft()
            visited+=1
            for child in graph[course]:
                in_deg[child]-=1
                if in_deg[child] == 0:
                    queue.append(child)
        return visited == numCourses
        