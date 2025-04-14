# link: https://leetcode.com/problems/course-schedule/
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = {key: [] for key in range(numCourses)}
        for i in prerequisites:
            coursemap[i[0]].append(i[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if coursemap[course] == []:
                return True 
            
            visited.add(course)
            for cor in coursemap[course]:
                value = dfs(cor)
                if value is False:
                    return False
            
            visited.remove(course)
            coursemap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i) : return False
        return True

# time complexity: O(V + E)
# space complexity: O(V)
# V is the number of courses
# E is the number of prerequisites