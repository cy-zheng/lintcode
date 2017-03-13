class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        queue = [start]
        visited = set([start])
        level = 0
        dict.add(start)
        dict.add(end)
        
        while queue:
            level += 1
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == end:
                    return level
                for item in self.find_neighbors(word, dict):
                    if item in visited:
                        continue
                    visited.add(item)
                    queue.append(item)
        
    def find_neighbors(self, word, dict):
        result = []
        for i in range(len(word)):
            code = ord(word[i])
            for j in range(97, 123):
                if j == code:
                    continue
                string = word[:i] + chr(j) + word[i + 1:]
                if string in dict:
                    result.append(string)
        return result