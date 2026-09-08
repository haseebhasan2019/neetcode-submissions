class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keep track of each course's in degree (number of prereqs)
        # enqueue all courses with an in deg of 0 (no prereqs)
        # when you explore courses with in deg 0, decrement in deg of their postreqs
        # and enqueue any with in degree of 0
        # if in-degree of all courses goes down to 0 then return true else false
        in_deg = [0] * numCourses
        # prereq [a,b] means b is a prereq of a
        post_reqs = defaultdict(list)
        for a, b in prerequisites:
           in_deg[a] += 1
           post_reqs[b].append(a)
        q = deque()
        completed = 0
        for course, deg in enumerate(in_deg):
            if deg == 0:
                q.append(course)
        while q:
            course = q.popleft()
            completed += 1
            for post_req in post_reqs[course]:
                in_deg[post_req] -= 1
                if in_deg[post_req] == 0:
                    q.append(post_req)

        return completed == numCourses
        
                
