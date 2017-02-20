class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        result = []
        if not candidates or target is None:
            return result
        candidates = sorted(list(set(candidates)))
        self.dfs(candidates, 0, [], result, target)
        return result
        
    def dfs(self, candidates, start_num, subset, result, target):
        if sum(subset) < target:
            for i in range(start_num, len(candidates)):
                subset.append(candidates[i])
                self.dfs(candidates, i, subset, result, target)
                subset.pop()
        elif sum(subset) == target:
            result.append(subset[:])