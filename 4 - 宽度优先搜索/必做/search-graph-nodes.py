# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        if not graph or not node or not values or target is None:
            return None
        queue = [node]
        while queue:
            nd = queue.pop(0)
            if values[nd] == target:
                return nd
            for neighbor in nd.neighbors:
                queue.append(neighbor)
        return None