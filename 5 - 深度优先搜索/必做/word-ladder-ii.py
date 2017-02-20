class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        # write your code here
        result = []
        if start is None or end is None or not dict:
            return result
        graph = self.bfs(dict, end)
        self.dfs(graph, [], start, end, result)
        for r in result:
            r.insert(0, start)
        return result
        
    def dfs(self, graph, path, start, end, result):
        if start == end:
            result.append(path[:])
        else:
            min_distance = 99999
            words = []
            for n in range(len(start)):
                for m in range(ord('a'), ord('z') + 1):
                    if start[n] == chr(m):
                        continue
                    temp = start[:n] + chr(m) + start[n + 1:]
                    if not (graph.get(temp, None) is None):
                        if graph.get(temp, None)['distance'] < min_distance:
                            words = [temp]
                            min_distance = graph.get(temp, None)['distance']
                        elif graph.get(temp, None)['distance'] == min_distance:
                            words.append(temp)
            for w in words:
                path.append(w)
                self.dfs(graph, path, w, end, result)
                path.pop()

            
        
    def bfs(self, dict, end):
        visited = {end: True}
        graph = {}
        queue = [end]
        level = -1
        for d in dict:
            visited.setdefault(d, False)
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                word = queue.pop(0)
                item = {
                            'neighbors': [],
                            'distance': level
                        }
                for n in range(len(word)):
                    for m in range(ord('a'), ord('z') + 1):
                        if word[n] == chr(m):
                            continue
                        temp = word[:n] + chr(m) + word[n + 1:]
                        if not (visited.get(temp, None) is None):
                            item['neighbors'].append(temp)
                            if not visited.get(temp, False):
                                visited[temp] = True
                                queue.append(temp)
                graph[word] = item
        return graph
        
    
                