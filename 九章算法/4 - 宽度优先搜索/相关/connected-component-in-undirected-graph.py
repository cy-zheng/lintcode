# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        queue = []
        visited = set([])
        results = []
        
        for node in nodes:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                result = [node.label]    
                while queue:
                    item = queue.pop(0)
                    for neighbor in item.neighbors:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                            result.append(neighbor.label)
                results.append(sorted(result))
        return results
            