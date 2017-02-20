class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        results = []
        if not S:
            return results
        S.sort()
        self.dfsHelper(S, 0, [], results)
        return results

    def dfsHelper(self, S, start_index, subset, results):
        results.append(subset[:])
        for i in range(start_index, len(S)):
            if i != start_index and subset.count(S[i]) != i - S.index(S[i]):
                continue
            subset.append(S[i])
            self.dfsHelper(S, i + 1, subset, results)
            subset.pop()