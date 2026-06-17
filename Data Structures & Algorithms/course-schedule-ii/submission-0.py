class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_deg = [0] * numCourses
        children_map = defaultdict(list)
        for course, prereq in prerequisites:
            in_deg[course]+=1
            children_map[prereq].append(course)
        visited = []
        queue = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            visited.append(course)
            for child in children_map[course]:
                in_deg[child]-=1
                if in_deg[child] == 0:
                    queue.append(child)
        return visited if len(visited) == numCourses else []