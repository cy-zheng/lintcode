class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        result = []
        if not candidates or target is None:
            return result
        candidates.sort()
        self.dfs(candidates, 0, [], result, target)
        return result
        
    def dfs(self, candidates, start_num, subset, result, target):
        if sum(subset) < target:
            for i in range(start_num, len(candidates)):
                if i > start_num and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                self.dfs(candidates, i + 1, subset, result, target)
                subset.pop()
        elif sum(subset) == target:
            result.append(subset[:])