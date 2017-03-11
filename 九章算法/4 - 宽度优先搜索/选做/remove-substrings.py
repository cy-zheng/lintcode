import sys
class Solution:
    # @param {string} s a string
    # @param {set} dict a set of n substrings
    # @return {int} the minimum length
    def minLength(self, s, dict):
        # Write your code here
        min_len = sys.maxint
        queue = [s]
        visited = set([])
        while queue:
            string = queue.pop(0)
            flag = False
            for substr in dict:
                index = self.strStr2(string, substr)
                if index:
                    flag = not flag
                    for item in index:
                        result = string[:item] + string[item + len(substr):]
                        if result not in visited:
                            queue.append(result)
                            visited.add(result)
            if not flag:
                min_len = min(min_len, len(string))
        return min_len
        
    def strStr2(self, source, target):
        # Write your code here
        result = []
        if not source:
            return result
        index = source.find(target)
        while index != -1:
            result.append(index)
            index = source.find(target, index + 1)
        return result