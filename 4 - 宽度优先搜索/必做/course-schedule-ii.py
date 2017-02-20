class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        graph = {}
        for i in range(numCourses):
            graph[i] = {'in': [], 'out': []}
        for p in prerequisites:
            graph[p[0]]['in'].append(p[1])
            graph[p[1]]['out'].append(p[0])
            
        queue = []
        for key in graph:
            if len(graph[key]['in']) == 0:
                queue.append(key)
        
        result = []        
        while queue:
            course = queue.pop(0)
            result.append(course)
            for key in graph[course]['out']:
                graph[key]['in'].remove(course)
                if len(graph[key]['in']) == 0:
                    queue.append(key)
                    
        if len(result) == numCourses:
            return result
        else:
            return []
            