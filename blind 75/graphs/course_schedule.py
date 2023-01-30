from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_reqs = defaultdict(list)

        for [a, b] in prerequisites:
            pre_reqs[a].append(b)
        
        satisfied = set()

        def dfs(course, visited):
            if course in satisfied:
                return True

            if course in visited:
                return False

            visited.add(course)

            if course in pre_reqs:
                for dependency in pre_reqs[course]:
                    if not dfs(dependency, visited): return False
            
            visited.remove(course)
            satisfied.add(course)
            
            return True

        for course in pre_reqs.keys():
            if dfs(course, visited = set())==False: return False
        
        return True

print(Solution().canFinish(2, [[1,0]]))

# cant do dfs with defaultdict
# return nothing does what?