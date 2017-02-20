# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return None
        nodes = self.bfs(node)
        
        map_new_node = {}
        for n in nodes:
            map_new_node[n] = UndirectedGraphNode(n.label)
            
        for n in nodes:
            for l in n.neighbors:
                map_new_node[n].neighbors.append(map_new_node[l])
            
        return map_new_node[node]
        
    def bfs(self, node):
        result = []
        if not node:
            return result
            
        queue = [node]
        node_set = set([])
        while queue:
            
            n = queue.pop(0)
            #从队列取出来的时候判断重复没有
            if n in node_set:
                continue
            result.append(n)
            node_set.add(n)
            for l in n.neighbors:
                queue.append(l)
                    
        return result
                    