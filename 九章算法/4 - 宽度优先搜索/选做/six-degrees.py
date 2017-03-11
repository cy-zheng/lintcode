# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):
        # Write your code here
        if not graph or not s or not t:
            return -1
            
        queue = [s]
        steps = 0
        visited = set([s])
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node == t:
                    return steps
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            steps += 1
        return -1