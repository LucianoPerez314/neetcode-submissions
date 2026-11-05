from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort using kahn's algorithm
        next_courses = defaultdict(list)
        in_degree = defaultdict(int)
        # build in degree and next courses lookup.
        for a, b in prerequisites:
            next_courses[b].append(a)
            in_degree[a] += 1
        # add courses with in_degree of 0 to the queue. These courses can be taken without prereqs.
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for next_course in next_courses[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # If all courses can't be completed return empty array.
        if len(res) != numCourses:
            return []

        # All courses can be completed so return the order.
        return res