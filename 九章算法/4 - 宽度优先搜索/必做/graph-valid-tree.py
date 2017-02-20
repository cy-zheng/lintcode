class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if not n or edges is None:
            return False
        if len(edges) != n - 1:
            return False
            
        graph = []
        for i in range(n):
            graph.append(set([]))
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            
        queue = [0]
        node_set = set([])
        
        while queue:
            key = queue.pop(0)
            node_set.add(key)
            for node in graph[key]:
                if node not in node_set:
                    queue.append(node)
                    
        return len(node_set) == n