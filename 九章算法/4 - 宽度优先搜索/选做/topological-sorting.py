# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        result = []
        if not graph:
            return result
            
        for node in graph:
            for n in node.neighbors:
                if hasattr(n, 'in_degree'):
                    n.in_degree += 1
                else:
                    n.in_degree = 1
        
        queue = []            
        for node in graph:
            if not hasattr(node, 'in_degree') or node.in_degree == 0:
                queue.append(node)
        while queue:
            node = queue.pop(0)
            result.append(node)
            for n in node.neighbors:
                n.in_degree -= 1
                if n.in_degree == 0:
                    queue.append(n)
        return result