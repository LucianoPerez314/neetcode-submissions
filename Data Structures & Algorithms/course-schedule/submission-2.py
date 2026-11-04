from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = defaultdict(int)
        next_courses = defaultdict(list)

        # compute the in degree an make a cleaner prerequisite map.
        for a, b in prerequisites:
            in_degrees[a] += 1
            next_courses[b].append(a)

        queue = deque()
        
        # add nodes with an in-degree of 0 to the queue since these courses can be taken without prereqs.
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)
        
        explored = set()
        while queue:
            course = queue.popleft()
            explored.add(course)
            
            for next_course in next_courses[course]:
                # decrement in-degree of the next courses since the prerequisite was completed.
                in_degrees[next_course] -= 1
                # if the in-degree is zero then these courses are now able to be taken. 
                if in_degrees[next_course] == 0:
                    queue.append(next_course)
        
        # explored containing all courses indicates all courses were taken. 
        return len(explored) == numCourses
        